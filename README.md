# 🥔Lang
An experiment with programming languages in base 1.

### The Vision

The set of all possible programs is countably infinite. As a result, we can give each possible program a number, and then represent it in base 1 (tally marks). 

The initial vision was to store each program as some number of potato emojis, but that quickly became infeasible, as storing the word "meow" in this way would take around 27 GB of space.

At the moment, this will just write the base 10 representation of a program to a file, and can reconstruct the program from that base 10 representation. Keep in mind that this number actually counts the number of potatoes needed to make this program.

### How it works

At the moment, the conversion code assumes each program is written in ASCII, or base 128. We can think of a program as a base 128 number, which we then must convert to base 10.

### Usage

To convert a file to 🥔Lang:

```
python3 convert.py --encode <inputFile> <outputFile>
```

To convert a 🥔Lang file back to a normal file:

```
python3 convert.py --decode <inputFile> <outputFile>
```

### Future Plans

At the moment, storing as a base 10 number is fast and not computationally intensive. By writing to a zip file, we could likely save a lot of space while still keeping the original vision alive, but this would create zip files that SHOULD NEVER BE OPENED UNDER ANY CIRCUMSTANCES and would end up taking a loooooong time to process.

Still a possibility though.



We could significantly reduce the space taken by this program by using a smaller character set. There are several Turing complete languages with a small character set (~8 characters). This is a likely next step.



Additionally, we would like to run the converted code directly, instead of simply writing out the decoded file.



Furthermore, because encoded files were taking up to much space, we had to remove all the potatoes 🥔 (and we did so very sadly :( ). We want to put them back one day.