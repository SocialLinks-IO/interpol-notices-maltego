# Interpol Notices transforms for Maltego

A list of transforms for searching Red, Yellow, and UNSC notices by Name or Phrase.

[Official source](https://www.interpol.int/How-we-work/Notices/View-Red-Notices), [API description](https://interpol.api.bund.dev/).

# How to use

## Import entities

Import Entities and Icons from `interpol.mtz` to your Maltego (thanks sinwindie!).

<img width="857" alt="Import" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/3af3451a-d95f-4b74-8783-ceb74b351a98">

Automatic congiguring of imported local transforms is a bit difficult and will be implemented later.

## Create transforms (manually)

Configure each file in transforms folder like this:

1. Press "New Local Transforms..." button

<img width="453" alt="Step 1" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/72047edc-a666-4aa2-8cee-9a49fd643066">

2. Fill in the fields in the first window

<img width="860" alt="Step 2" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/4cbc8be1-7b12-4dc3-bdcf-901d7816abd1">

3. Fill in the fields in the second window

<img width="860" alt="Step 3" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/1377825c-e63b-40ff-b8dd-031dc0752769">

# Running

Create Person entity for searching by namme. Be sure you've entered first/last name in the right order, change it if you don't get results.

Create Phrase entity for searching by keyword OR part of name, even for mentioned relatives.

<img width="703" alt="Example of usage" src="https://github.com/soxoj/interpol-notices-maltego/assets/31013580/4998ddac-7e6a-4bf5-9c2c-2e5eff859b37">

## TODO

- [ ] Face search transforms / converters
- [ ] Local transforms configuring automation
- [ ] Test examples

=======
## Credits

**Many thanks to OSINT Dojo / Sinwindie for entities, icons and initial source code: https://github.com/OsintDojo/public**
