# Badger 2040 Schedule

This turns your Badger into a portable conference schedule viewer.

![Badger Schedule in action](https://github.com/creativenucleus/badger-2040-schedule/blob/main/readme/badger-schedule.gif?raw=true)

Configure the talks for a day, and skip forward and back with the face buttons.  
Marvel at the progress bar at the bottom of the Badger.

This program requires some assets to be built (that is: images cropped and transformed). There is a Windows `.bat` file supplied to do this. If you're using another OS, you'll need to roll your own. Please fork/pull-request and contribute it back :)

Clarifications to this readme also welcome by fork/pull-request.

Use at your own risk, etc.

## Building

### System Setup

1. Install [Thonny](https://thonny.org/), which is used to compile and deliver MicroPython to the Badger.
2. Install [ImageMagick](https://imagemagick.org/script/index.php) for resizing/cropping images. The `magick` command should be available to the command line.  
3. Ensure `python3` can be called from the command line. [Install](https://www.python.org/downloads/) it if it's not available.
4. Copy [this Image Converter script](https://github.com/pimoroni/pimoroni-pico/blob/main/examples/badger2040/image_converter/convert.py) into the `external-code` folder.
5. The conversion script has a dependency. Use `pip3 install pillow` to install it.

### Configuration

An example is provided so you should be able to be running straight away. A skeleton is supplied so you can create your own schedule data to load.

#### To use the example as-is

1. Copy the contents of the `config-example` folder into `config`

#### To setup your own

1. Copy the contents of the `config-example` folder into `config`
2. Add your own images into the `config/images` folder.
3. Edit `config/config.py` to describe the day's schedule.

### Building assets (run the first time and when source images or schedule change)

The Badger requires image assets to be compiled in a particular format. The build chain will have a crack at resizing, cropping, and converting images, leaving the originals untouched.

1. Run `build-win.bat`. This should create a `_deploy` folder containing a `cn_schedule` folder which has an `images` subfolder and your `config.py` file.

### Deploying to Badger
1. Open Thonny.
2. Attach your Badger via USB.
3. Ensure Thonny is set up to deploy to [Badger](https://learn.pimoroni.com/article/getting-started-with-badger-2040#programming-badger-with-thonny). Particularly, ensure the bottom right of the window says `MicroPython (Raspberry Pi Pico)` - change this by click-and-select if it does not.
4. Ensure the file browser is open in Thonny (in the menu: View -> Files should be ticked)
5. In the bottom browser pane (this is the Badger) delete `cn_schedule` folder if it exists.
6. Find the `_deploy` folder on your computer (the top file browser pane).
7. Right click `_deploy/cn_schedule` and click `upload to /`
8. Open `badge.py` in Thonny.
9. Hit the `Run Current Script` button. This will load `badge.py` onto Badger and run it.

## All gone well?

Please send me a message / picture / video of your Badger :)  
[Twitter: @jtruk](https://twitter.com/jtruk)
[Mastodon: @jtruk@mastodon.social](https://mastodon.social/@jtruk)
[Web: creativenucleus.com](https://www.creativenucleus.com)

## References

### General info / Hat tips
- [Getting Started With Badger (Pimoroni)](https://learn.pimoroni.com/article/getting-started-with-badger-2040)
- [Setting up Badger (Thought Asylum)](https://www.thoughtasylum.com/2022/04/29/the-badger-2040-set-up/)

## License

You're welcome to lift any code you like, fork, or adapt. Please respect [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) for any significant chunks of code (Assertion: James Rutherford / creativenucleus 2022).
