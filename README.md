# Python bindings for Oculus SDK

Based on `PyBindGen`, we auto-generate the Python bindings based on the `ovr_sdk` source headers.

## Dependencies

- Oculus SDK (e.g. `ovr_sdk_linux_0.4.4.tar.gz`). Ideally we can re-generate when a new version of the SDK is released
- System `gccxml` (i.e. `sudo apt-get install gccxml`)
-`pygccxml` version 1.5.2, due to [this bug](https://bugs.launchpad.net/pybindgen/+bug/1348785) with newer versions of pygccxml.


## Usage

I recommend a using `virtualenv`, so you can install pygccxml and this module in an isolated manner.

To generate the bindings, run

    python bindings_generator.py 'path-to-ovr_sdk'

Then, in theory you can install the module using:

    python setup.py install

**Note** that this install is *not currently working*.
