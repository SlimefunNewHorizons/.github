"""Exercise descriptor handling without downloads or starting a server."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile


SCRIPT = Path(__file__).with_name("server-smoke-test.sh")


class DescriptorTests(unittest.TestCase):
    def run_fixture(self, descriptors):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            jar = root / "fixture.jar"
            with zipfile.ZipFile(jar, "w") as archive:
                for name, text in descriptors.items():
                    archive.writestr(name, text)
            tools = root / "bin"
            tools.mkdir()
            curl = tools / "curl"
            curl.write_text("#!/bin/sh\nexit 42\n")
            curl.chmod(0o755)
            result = subprocess.run(
                ["bash", str(SCRIPT), "fixture", str(jar)], cwd=root,
                env={**os.environ, "PATH": str(tools) + os.pathsep + os.environ["PATH"]},
                capture_output=True, text=True, timeout=5,
            )
            return result, (root / "server-fixture").exists()

    def assert_descriptor(self, files, expected):
        result, created = self.run_fixture(files)
        self.assertEqual(42, result.returncode, result.stderr)
        self.assertIn("Plugin a probar: " + expected, result.stdout)
        self.assertTrue(created)
        self.assertNotIn("filename not matched", result.stderr)

    def test_bukkit_descriptor(self):
        self.assert_descriptor({"plugin.yml": "name: LegacyPlugin\n"}, "LegacyPlugin")

    def test_paper_descriptor(self):
        self.assert_descriptor({"paper-plugin.yml": "name: PaperPlugin\n"}, "PaperPlugin")

    def test_paper_descriptor_has_priority(self):
        self.assert_descriptor({"paper-plugin.yml": "name: PaperPlugin\n",
                                "plugin.yml": "name: LegacyPlugin\n"}, "PaperPlugin")

    def test_single_quotes(self):
        self.assert_descriptor({"paper-plugin.yml": "name: 'PaperPlugin'\n"}, "PaperPlugin")

    def test_double_quotes(self):
        self.assert_descriptor({"plugin.yml": 'name: "LegacyPlugin"\n'}, "LegacyPlugin")

    def test_missing_descriptors(self):
        result, created = self.run_fixture({"README": "fixture"})
        self.assertEqual(1, result.returncode)
        self.assertIn("paper-plugin.yml o plugin.yml", result.stderr)
        self.assertFalse(created)

    def test_missing_name(self):
        result, created = self.run_fixture({"paper-plugin.yml": "version: 1\n"})
        self.assertEqual(1, result.returncode)
        self.assertFalse(created)

    def test_empty_paper_descriptor_does_not_hide_behind_legacy(self):
        result, created = self.run_fixture({"paper-plugin.yml": "",
                                           "plugin.yml": "name: LegacyPlugin\n"})
        self.assertEqual(1, result.returncode)
        self.assertFalse(created)

    def test_shared_reader_preserves_version_for_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            jar = Path(directory) / "fixture.jar"
            metadata = 'name: PaperPlugin\nversion: "1.1-SNAPSHOT"\n'
            with zipfile.ZipFile(jar, "w") as archive:
                archive.writestr("paper-plugin.yml", metadata)
            result = subprocess.run(
                ["bash", str(SCRIPT.with_name("plugin-descriptor.sh")), str(jar)],
                capture_output=True, text=True, timeout=5,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual(metadata, result.stdout)


if __name__ == "__main__":
    unittest.main()
