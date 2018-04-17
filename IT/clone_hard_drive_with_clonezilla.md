# Clone a hard drive with Clonezilla

These are notes from the field, sorry for incompleteness.

You need:

- A USB stick with live clonezilla (see [here](https://clonezilla.org/liveusb.php) how to create one)
- A USB hard drive with 40Go or more depending on how full the computer is (it will tell you how much will get used). 

Process:

- Turn the computer off
- Plug the Clonezilla stick
- Boot the computer, on boot screen press whatever keys give you BIOS access.
- Ask to boot on the USB stick.
- Once on the Clonezilla splash page, always press enter unless mentioned otherwise below:
  - Choose ``device-image``
  - Use ``local_device``
  - Make sure the external hard drive is detected before pressing the Ctrl+C to continue.
  - On the "Now we need to mount a device" screen, select your external hard drive.
  - Choose ``expert mode``.
  - Choose option ``q2``.
  - Don't change volume size (4096).
  - Choose fsck (but not Auto-repair as it is dangerous).
  - Choose "wait at the end" so you can come back to the computer and check that everything went ok.
