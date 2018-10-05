# nso-pathtrace

A simple NSO python service which allows a user to configure
pathtrace objects which contain a device and a destination IP
address.

The service also provides a "run" action which will then execute a
ping and traceroute from the services' device to the desination IP
and return results to the NSO console.

# Installation

From your runtime packages directory
```
git clone https://github.com/kecorbin/nso-pathtrace pathtrace
cd pathtrace/src
make clean all
```

From `ncs_cli`

```
packages reload
```

# Credits

This is a generated Python package, made by:

  ncs-make-package --service-skeleton python \
                   --component-class main.Main pathtrace

It contains a dummy YANG model which implements a minimal Service
and an Action that doesn't really do anything useful. They are
there just to get you going.

# Testing

You will also find two test cases in:

  test/internal/lux/service/
  test/internal/lux/action/

that you can run if you have the 'lux' testing tool.
Your top Makefile also need to implement some Make targets
as described in the Makefiles of the test cases.
You can also just read the corresponding run.lux tests and
do them manually if you wish.

The 'lux' test tool can be obtained from:

  https://github.com/hawk/lux.git
