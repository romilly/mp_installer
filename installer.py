#! /user/bin/env python3
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

    def install_upython(self):
        if not self.pico_dir.exists():
            self.enter_bootloader()
        for i in range(10):
            try:
                path = self.location.joinpath('uf2/rp2-pico-w-latest.uf2')
                shutil.copy(path, self.pico_dir)
                break
            except PermissionError:
                time.sleep(1)
                continue
        self.wait_for_pico_dir(False)


def print_usage_and_exit():
    print('usage installer.py [nuke]')
    sys.exit(1)


if __name__ == '__main__':
    i = Installer()
    if len(sys.argv) not in [1, 2]:
        print_usage_and_exit()
    if len(sys.argv) == 2:
        if sys.argv[2] != 'nuke':
            print_usage_and_exit()
        i.nuke()
    i.install_upython()