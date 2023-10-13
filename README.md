# HW5. Modules

> *This is repository for the fifth homework assignment of the BI Python 2023 course*
## Table of contents

  * [Project description](#project-description)
  * [Main part](#Main-part)
  * [Usage](#Usage)
  * [Parametrs](#Parameters)
  * [Examples](#examples)
  * [Requirements](#Requirements)
  * [Contact](#contact)
  * [Educational result](#Учебный-результат)
  * [See also](#see-also)

## Project Description
This project includes several projects, and the first thought that came to my mind when viewing the task was ~~это starдец~~ it would be difficult. By that time I had neither 3 nor 4 homework assignments. But I didn't have time to cry. To reach the goal, a person needs only one thing – to go. Slowly I did 3 homework, then I got to 4 and now I have reached the writing of the README file of the fifth homework

![go to goal](https://st3.depositphotos.com/1001201/12919/i/450/depositphotos_129195498-stock-photo-businessman-running-fast.jpg)

## Main part
This project consists of 2 points; it combines 3 mini-projects from previous tasks [HERE](https://github.com/1799mrd/HW4_Functions2/tree/HW4_Mukhametshina), [HERE](https://github.com/Python-BI-2023/hw3-functions-1799mrd/tree/develop) and [HERE](https://github.com/1799mrd/Bioinformatic_tools/blob/develop/all_functions/fastq_filtration_tools.py). 
In this work need to get a real package with bioinformatics utilities. </br>

There are 2 points in this project:

### Writing a utility for working with fastq sequences. 
The main function takes 4 arguments as input: `seqs`, `gc_bounds`, `length_bounds`, `quality_threshold`:

- `seqs` - a dictionary consisting of fastq sequences. The structure is as follows. Key - string, sequence name. The value is a tuple of two strings: sequence and quality. Since I haven’t read files yet, we use a python dictionary.
The `example_data.py` script contains an example for debugging.
- `gc_bounds` - GC composition interval (in percentage) for filtering (by default it is equal to (0, 100), i.e. all reads are saved). If you pass one number as an argument, it is considered to be the upper limit. Examples: `gc_bounds = (20, 80)` - we save only reads with GC content from 20 to 80%, `gc_bounds = 44.4` - we save reads with GC content less than 44.4%.
- `length_bounds` - length interval for filtering, everything is similar to `gc_bounds`, but by default it is (0, 2**32).
- `quality_threshold` - the threshold value of the average quality of the read for filtering, by default it is 0 (phred33 scale). Reads with average quality across all nucleotides below the threshold are discarded. </br></br> 


**Based on the results of the work** the main function returns a similar dictionary, consisting only of those sequences that pass all the conditions. All described intervals include both upper and lower boundaries. </br>


### Assembling projects for working with fastq sequences, amino acid sequences, DNA and RNA sequences. 
HERE HERE AND HERE into a single package for a novice bioinformatician

    ```python
    -/
     |- bioinf_script.py # (импорты и 3 функции)
     |- README.md
     |- all_functions/
           |- amino_acid_tools.py # (ДНК-функции)
           |- dna_rna_tools.py # (белковые функции)
           |- fastq_filtration_tools.py # (FASTQ-функции)
    ``` 

# Bioinformatic tool - DNA/RNA sequence processing/amino acid sequence processing/fastq sequences filtering 
This tool is designed to work with fastq sequences, amino acid sequences, DNA and RNA sequences.

## Usage   
There three functions: `filter_fastq_sequences`, `amino_acid_tools`, `run_dna_rna_tools`.

If you are working with fastq sequences, run `filter_fastq_sequences` function </br>
It takes as input a dictionary containing an unlimited number of fastq sequences, filtering bounds on gc composition, length, and average read quality. The function then filters all sequences in the dictionary. Sequences can contain both uppercase and lowercase letters. The result of the function is a dictionary with filtered sequences.

If you are working with amino acid sequences, run `amino_acid_tools` function </br>
It takes as input an arbitrary number of arguments with amino acid sequences (str) as well as the name of the procedure to be performed.

If you are working with dna or rna sequences, run `run_dna_rna_tools` function </br> 
It takes as input an arbitrary number of arguments with DNA or RNA sequences (str) and the name of the procedure to be performed. 

For `amino_acid_tools` and `run_dna_rna_tools` input sequences can contain both uppercase and lowercase letters, but the last argument with the function name must match the possible functions. After that the command performs the specified action on all the given sequences. If one sequence is submitted, a string with the result is returned. If several sequences are submitted, a list of strings is returned.


## Parameters 

#### For `filter_fastq_sequences` function

Function works with fastq file: </br>
##### Parameters: </br> `seqs`, `gc_bounds`, `length_bounds`, `quality_threshold`: </br>
- **seqs** is a dictionary consisting of fastq sequences. The structure is as follows. The key is a string, the name of the sequence. The value is a tuple of two strings: sequence and quality. In fact, this is the content of a fastq file, but you and I have not yet been through reading files. So for now we are using a python dictionary. Then it will be enough to add reading files and writing them to a dictionary of this kind so that everything works from beginning to end. In the script `example_data.py ` an example has been made for you to debug. </br>
- **gc_bounds** - GC composition interval (in percent) for filtering (by default is (0, 100), i.e. all reads are saved). If a single number is passed to the argument, it is assumed that this is the upper bound. Examples: `gc_bounds = (20, 80)` - save only reads with GC composition from 20 to 80%, `gc_bounds = 44.4` - save reads with GC composition less than 44.4%. </br>
- **length_bounds** - the length interval for filtering, everything is similar to `gc_bounds`, but by default it is `(0, 2**32)`. </br>
- **quality_threshold** is the threshold value of the average quality of the read for filtering, by default it is 0 (phred33 scale). Reads with average quality for all nucleotides below the threshold are discarded. </br></br>
##### Return: </br>
`similar dictionary` consisting only of those sequences that have passed all the conditions. All the described intervals include both upper and lower bounds.   

#### For `amino_acid_tools` function
The following options for amino acid sequence processing are available at the moment: </br>
##### Parametrs:
-  `molecular weight`: calculates the molecular weight of an amino acid chain
-  `long_amino_code`: converts translations from one letter to translations from three letters
-  `amino_to_rna` : translates a sequence of amino acids into a possible sequence of nucleic acids
-  `amino_seq_charge`: estimates the total charge of the amino acid chain in a neutral aqueous solution (pH = 7)
##### Return:
If one sequence is supplied, a string with the result is returned. </br>
If several are submitted, a list of strings is returned. </br>
Depending on the function performed, the following returns will occur:
-  `long_amino_code` (str) or (list): translated sequence from one-letter in three-letter code
-  `molecular_weight` (int) or (list): amino acid sequence molecular weight number or list of numbers
-  `amino_to_rna` (str) or (list): possible RNA sequence
-  `amino_seq_charge` (str) or (list): "positive", "negative" or "neutral"

#### For `run_dna_rna_tools` function
- **transcribe**: print transcribed sequence
- **reverse**: print reversed sequence
- **complement**: print complementary sequence
- **reverse_complement**: print reverse complementary sequence

## Examples

### For `filter_fastq_sequences` function
Below is an example of processing a fastq sequences.
```python
EXAMPLE_FASTQ = {
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079804:1:SRR292678:1:1101:149302:149302': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079804:1:SRR292678:1:1101:170868:170868': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
    }
filter_fastq = filter_fastq_sequences(EXAMPLE_FASTQ, (20, 80), (0, 80), 30)
print(filter_fastq)

#{'@SRX079804:1:SRR292678:1:1101:170868:170868': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', #'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
#'@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', #'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
#'@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', #'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
#'@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', #'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
#'@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', #'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
#'@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG','<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')}
```

### For `amino_acid_tools` function
Below is an example of processing an amino acid sequence.

```python
Using the function for translated sequence from one-letter in three-letter code:
amino_acid_tools('PLfHnfPdD','long_amino_code') # 'ProLeuPheHisAsnPheProAspAsp'
amino_acid_tools('random', 'CpUPQWhmrY','molecular_weight')  # [('рандомная последовательнсть', 'FySiDfGym', 1124.43), 1367.39]
amino_acid_tools('cvdrLepaW', 'amino_to_rna')  # 'ugugucgaccggCUAgagccggcgUGG'
amino_acid_tools('cvdrLepaW', 'VurgdOhio', 'amino_seq_charge') # ['negativ', 'positiv']
```

#### For `run_dna_rna_tools` function
Below is an example of processing DNA and RNA sequences.

```python
run_dna_rna_tools('ATG', 'transcribe') # 'AUG'
run_dna_rna_tools('ATG', 'reverse') # 'GTA'
run_dna_rna_tools('AtG', 'complement') # 'TaC'
run_dna_rna_tools('ATg', 'reverse_complement') # 'cAT'
run_dna_rna_tools('ATG', 'aT', 'reverse') # ['GTA', 'Ta']
```

## Requirements
You need to import modules:
```python
from all_functions.amino_acid_tools import amino_acid_tools
from all_functions.dna_rna_tools import run_dna_rna_tools
from all_functions.fastq_filtration_tools import filter_fastq_sequences
```
## Учебный-результат
> * В данном проекте я научилась пользоваться pyCharm в котором довольно удобно писать Readme file. А также работу с модулями
> * К сожалению, я не успела получить комментарии к 4 дз и не смогла исправить код к данному проекту, но перечитать все написанное мной пришлось.
> * Вспомнила fastq

## Contacts  
- [Mukhametshina Regina] 1709mrd@gmail.com

![health](https://u.9111s.ru/uploads/202209/12/27ec4ad913eaa7cf6277658d30dbb3cf.jpg)

## See also 

Про fastq-файлы можно посмотреть, например, [здесь](https://stepik.org/lesson/32398/step/1?unit=12379), про определение качества на основе ASCII-кода можно почитать [здесь](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm), также вам может пригодиться таблица [кодировки ASCII](https://www.asciitable.com/) и функция ord (документация [en](https://docs.python.org/3/library/functions.html#ord), [ru](https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-ord/)).
