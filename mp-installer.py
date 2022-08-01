#! /usr/bin/env python3
import getpass
import pathlib
import shutil
import subprocess
import time
import sys


class Installer:
    def __init__(self):
        self.pico_dir = pathlib.Path('/media/%s/RPI-RP2/' % getpass.getuser())
        self.location = pathlib.Path(__file__).parent

    def enter_bootloader(self):
        if self. pico_dir.exists():
            return
        subprocess.run(['mpremote', 'bootloader'])
        self.wait_for_pico_dir()

    def wait_for_pico_dir(self, wanted=True):
        while self.pico_dir.exists() == wanted:
            time.sleep(1)

    def nuke(self):
        self.enter_bootloader()
        shutil.copy(self.location.joinpath('uf2/flash_nuke.uf2'), self.pico_dir)
        time.sleep(1)
        self.wait_for_pico_dir()

    def install_upython(self, uf2_path):
        print('installing %s' % uf2_path)
        if not self.pico_dir.exists():
            self.enter_bootloader()
        for i in range(10):
            try:
                shutil.copy(uf2_path, self.pico_dir)
                break
            except PermissionError:
                time.sleep(1)
                continue
        self.wait_for_pico_dir(False)


def print_usage_and_exit():
    print('usage mp-installer.py <uf2 file> [nuke]')
    sys.exit(1)


if __name__ == '__main__':
    i = Installer()
    if len(sys.argv) not in [2, 3]:
        print_usage_and_exit()
    uf2_path = pathlib.Path(sys.argv[1])
    if not uf2_path.exists():
        print("can't find %s")
        print_usage_and_exit()
    if len(sys.argv) == 3:
        if sys.argv[2] != 'nuke':
            print_usage_and_exit()
        print('nuking rpi filesystem')
        i.nuke()
    i.install_upython(uf2_path)