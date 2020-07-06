# rpm_device is the name of the ported device
%define rpm_device fp3
# rpm_vendor is used in the rpm space
%define rpm_vendor fairphone
# Manufacturer and device name to be shown in UI
%define vendor_pretty Fairphone
%define device_pretty Fairphone 3

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_native_vibrator 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc
