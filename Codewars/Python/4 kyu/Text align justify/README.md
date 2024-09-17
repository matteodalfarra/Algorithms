# Kata: [Text align justify](https://www.codewars.com/kata/537e18b6147aa838f600001b)

## Description
Your task is to implement a function that emulates text justification for monospace fonts. Given a single-line text and an expected width, the function should justify the text according to the following rules:

- Use spaces to fill the gaps between words.
- Each line should contain as many words as possible.
- Separate lines with the newline character `\n`.
- The last line should not end with a `\n`.
- Gaps between words should not differ by more than one space.
- Lines should end with a word, not a space.
- Larger gaps should go first, followed by smaller gaps.
- The last line should not be justified and should contain only one space between words.
- Lines with only one word don't need spaces.

### Example
With width=30:
```
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
```

### Input:
- A string of text (single line).
- An integer representing the width of the justification.

### Output:
- A string representing the justified text.