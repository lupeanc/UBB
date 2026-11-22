# Generated from grammar/Cinematography.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,460,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,5,0,92,8,0,
        10,0,12,0,95,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,110,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,5,4,128,8,4,10,4,12,4,131,9,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,142,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,
        8,1,8,5,8,154,8,8,10,8,12,8,157,9,8,1,9,1,9,1,9,5,9,162,8,9,10,9,
        12,9,165,9,9,1,10,1,10,1,10,1,10,3,10,171,8,10,1,11,1,11,1,11,5,
        11,176,8,11,10,11,12,11,179,9,11,1,12,1,12,1,12,5,12,184,8,12,10,
        12,12,12,187,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,196,8,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,206,8,13,1,14,1,
        14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,221,
        8,16,10,16,12,16,224,9,16,3,16,226,8,16,1,17,1,17,3,17,230,8,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,239,8,18,10,18,12,18,242,
        9,18,1,18,1,18,1,18,1,18,5,18,248,8,18,10,18,12,18,251,9,18,1,18,
        3,18,254,8,18,1,19,1,19,1,20,1,20,1,20,5,20,261,8,20,10,20,12,20,
        264,9,20,1,21,1,21,1,21,5,21,269,8,21,10,21,12,21,272,9,21,1,22,
        1,22,1,22,1,22,1,22,1,22,3,22,280,8,22,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,5,23,293,8,23,10,23,12,23,296,9,23,
        1,23,1,23,1,24,1,24,1,24,1,24,3,24,304,8,24,1,25,1,25,1,25,1,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,317,8,26,10,26,12,26,320,
        9,26,1,26,1,26,1,27,1,27,1,27,1,27,5,27,328,8,27,10,27,12,27,331,
        9,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,
        3,29,345,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,5,32,363,8,32,10,32,12,32,366,9,32,
        3,32,368,8,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,
        405,8,36,10,36,12,36,408,9,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,1,36,5,36,420,8,36,10,36,12,36,423,9,36,1,36,1,36,3,36,
        427,8,36,1,37,1,37,1,37,5,37,432,8,37,10,37,12,37,435,9,37,3,37,
        437,8,37,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,41,1,41,
        1,41,1,41,3,41,452,8,41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,0,0,45,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        0,5,1,0,23,24,1,0,25,27,1,0,1,4,1,0,8,9,1,0,28,33,466,0,93,1,0,0,
        0,2,109,1,0,0,0,4,111,1,0,0,0,6,117,1,0,0,0,8,123,1,0,0,0,10,141,
        1,0,0,0,12,143,1,0,0,0,14,148,1,0,0,0,16,150,1,0,0,0,18,158,1,0,
        0,0,20,166,1,0,0,0,22,172,1,0,0,0,24,180,1,0,0,0,26,205,1,0,0,0,
        28,207,1,0,0,0,30,212,1,0,0,0,32,225,1,0,0,0,34,229,1,0,0,0,36,231,
        1,0,0,0,38,255,1,0,0,0,40,257,1,0,0,0,42,265,1,0,0,0,44,279,1,0,
        0,0,46,281,1,0,0,0,48,303,1,0,0,0,50,305,1,0,0,0,52,309,1,0,0,0,
        54,323,1,0,0,0,56,335,1,0,0,0,58,344,1,0,0,0,60,346,1,0,0,0,62,353,
        1,0,0,0,64,358,1,0,0,0,66,371,1,0,0,0,68,379,1,0,0,0,70,387,1,0,
        0,0,72,426,1,0,0,0,74,436,1,0,0,0,76,438,1,0,0,0,78,441,1,0,0,0,
        80,445,1,0,0,0,82,451,1,0,0,0,84,453,1,0,0,0,86,455,1,0,0,0,88,457,
        1,0,0,0,90,92,3,2,1,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,
        93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,0,0,1,97,1,1,0,
        0,0,98,110,3,4,2,0,99,110,3,6,3,0,100,110,3,8,4,0,101,110,3,12,6,
        0,102,110,3,36,18,0,103,110,3,46,23,0,104,110,3,52,26,0,105,110,
        3,54,27,0,106,110,3,58,29,0,107,110,3,72,36,0,108,110,3,78,39,0,
        109,98,1,0,0,0,109,99,1,0,0,0,109,100,1,0,0,0,109,101,1,0,0,0,109,
        102,1,0,0,0,109,103,1,0,0,0,109,104,1,0,0,0,109,105,1,0,0,0,109,
        106,1,0,0,0,109,107,1,0,0,0,109,108,1,0,0,0,110,3,1,0,0,0,111,112,
        5,6,0,0,112,113,5,37,0,0,113,114,3,88,44,0,114,115,5,38,0,0,115,
        116,5,42,0,0,116,5,1,0,0,0,117,118,5,7,0,0,118,119,5,37,0,0,119,
        120,3,14,7,0,120,121,5,38,0,0,121,122,5,42,0,0,122,7,1,0,0,0,123,
        124,3,10,5,0,124,129,3,88,44,0,125,126,5,43,0,0,126,128,3,88,44,
        0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,
        0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,5,42,0,0,133,9,1,0,0,0,
        134,142,3,80,40,0,135,142,3,88,44,0,136,137,5,16,0,0,137,138,5,37,
        0,0,138,139,3,10,5,0,139,140,5,38,0,0,140,142,1,0,0,0,141,134,1,
        0,0,0,141,135,1,0,0,0,141,136,1,0,0,0,142,11,1,0,0,0,143,144,3,88,
        44,0,144,145,5,34,0,0,145,146,3,14,7,0,146,147,5,42,0,0,147,13,1,
        0,0,0,148,149,3,16,8,0,149,15,1,0,0,0,150,155,3,18,9,0,151,152,5,
        36,0,0,152,154,3,18,9,0,153,151,1,0,0,0,154,157,1,0,0,0,155,153,
        1,0,0,0,155,156,1,0,0,0,156,17,1,0,0,0,157,155,1,0,0,0,158,163,3,
        20,10,0,159,160,5,35,0,0,160,162,3,20,10,0,161,159,1,0,0,0,162,165,
        1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,19,1,0,0,0,165,163,1,
        0,0,0,166,170,3,22,11,0,167,168,3,86,43,0,168,169,3,22,11,0,169,
        171,1,0,0,0,170,167,1,0,0,0,170,171,1,0,0,0,171,21,1,0,0,0,172,177,
        3,24,12,0,173,174,7,0,0,0,174,176,3,24,12,0,175,173,1,0,0,0,176,
        179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,23,1,0,0,0,179,177,
        1,0,0,0,180,185,3,26,13,0,181,182,7,1,0,0,182,184,3,26,13,0,183,
        181,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,
        25,1,0,0,0,187,185,1,0,0,0,188,195,3,88,44,0,189,190,5,44,0,0,190,
        191,5,20,0,0,191,192,5,37,0,0,192,193,3,34,17,0,193,194,5,38,0,0,
        194,196,1,0,0,0,195,189,1,0,0,0,195,196,1,0,0,0,196,206,1,0,0,0,
        197,206,3,82,41,0,198,199,5,5,0,0,199,206,3,28,14,0,200,206,3,30,
        15,0,201,202,5,37,0,0,202,203,3,14,7,0,203,204,5,38,0,0,204,206,
        1,0,0,0,205,188,1,0,0,0,205,197,1,0,0,0,205,198,1,0,0,0,205,200,
        1,0,0,0,205,201,1,0,0,0,206,27,1,0,0,0,207,208,3,88,44,0,208,209,
        5,37,0,0,209,210,3,32,16,0,210,211,5,38,0,0,211,29,1,0,0,0,212,213,
        3,88,44,0,213,214,5,37,0,0,214,215,3,32,16,0,215,216,5,38,0,0,216,
        31,1,0,0,0,217,222,3,14,7,0,218,219,5,43,0,0,219,221,3,14,7,0,220,
        218,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,
        226,1,0,0,0,224,222,1,0,0,0,225,217,1,0,0,0,225,226,1,0,0,0,226,
        33,1,0,0,0,227,230,5,46,0,0,228,230,3,88,44,0,229,227,1,0,0,0,229,
        228,1,0,0,0,230,35,1,0,0,0,231,232,5,10,0,0,232,233,5,37,0,0,233,
        234,3,38,19,0,234,235,5,38,0,0,235,236,5,13,0,0,236,240,5,39,0,0,
        237,239,3,2,1,0,238,237,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,
        240,241,1,0,0,0,241,243,1,0,0,0,242,240,1,0,0,0,243,253,5,40,0,0,
        244,245,5,11,0,0,245,249,5,39,0,0,246,248,3,2,1,0,247,246,1,0,0,
        0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,252,1,0,0,
        0,251,249,1,0,0,0,252,254,5,40,0,0,253,244,1,0,0,0,253,254,1,0,0,
        0,254,37,1,0,0,0,255,256,3,40,20,0,256,39,1,0,0,0,257,262,3,42,21,
        0,258,259,5,36,0,0,259,261,3,42,21,0,260,258,1,0,0,0,261,264,1,0,
        0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,41,1,0,0,0,264,262,1,0,0,
        0,265,270,3,44,22,0,266,267,5,35,0,0,267,269,3,44,22,0,268,266,1,
        0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,43,1,0,
        0,0,272,270,1,0,0,0,273,280,3,20,10,0,274,280,3,84,42,0,275,276,
        5,37,0,0,276,277,3,38,19,0,277,278,5,38,0,0,278,280,1,0,0,0,279,
        273,1,0,0,0,279,274,1,0,0,0,279,275,1,0,0,0,280,45,1,0,0,0,281,282,
        5,12,0,0,282,283,5,37,0,0,283,284,3,48,24,0,284,285,5,42,0,0,285,
        286,3,38,19,0,286,287,5,42,0,0,287,288,3,50,25,0,288,289,5,38,0,
        0,289,290,5,13,0,0,290,294,5,39,0,0,291,293,3,2,1,0,292,291,1,0,
        0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,297,1,0,
        0,0,296,294,1,0,0,0,297,298,5,40,0,0,298,47,1,0,0,0,299,300,3,10,
        5,0,300,301,3,88,44,0,301,304,1,0,0,0,302,304,3,50,25,0,303,299,
        1,0,0,0,303,302,1,0,0,0,304,49,1,0,0,0,305,306,3,88,44,0,306,307,
        5,34,0,0,307,308,3,14,7,0,308,51,1,0,0,0,309,310,5,14,0,0,310,311,
        5,37,0,0,311,312,3,38,19,0,312,313,5,38,0,0,313,314,5,13,0,0,314,
        318,5,39,0,0,315,317,3,2,1,0,316,315,1,0,0,0,317,320,1,0,0,0,318,
        316,1,0,0,0,318,319,1,0,0,0,319,321,1,0,0,0,320,318,1,0,0,0,321,
        322,5,40,0,0,322,53,1,0,0,0,323,324,5,15,0,0,324,325,3,88,44,0,325,
        329,5,39,0,0,326,328,3,56,28,0,327,326,1,0,0,0,328,331,1,0,0,0,329,
        327,1,0,0,0,329,330,1,0,0,0,330,332,1,0,0,0,331,329,1,0,0,0,332,
        333,5,40,0,0,333,334,5,42,0,0,334,55,1,0,0,0,335,336,3,10,5,0,336,
        337,3,88,44,0,337,338,5,42,0,0,338,57,1,0,0,0,339,345,3,60,30,0,
        340,345,3,62,31,0,341,345,3,66,33,0,342,345,3,68,34,0,343,345,3,
        70,35,0,344,339,1,0,0,0,344,340,1,0,0,0,344,341,1,0,0,0,344,342,
        1,0,0,0,344,343,1,0,0,0,345,59,1,0,0,0,346,347,5,16,0,0,347,348,
        5,37,0,0,348,349,3,10,5,0,349,350,5,38,0,0,350,351,3,88,44,0,351,
        352,5,42,0,0,352,61,1,0,0,0,353,354,3,88,44,0,354,355,5,34,0,0,355,
        356,3,64,32,0,356,357,5,42,0,0,357,63,1,0,0,0,358,367,5,39,0,0,359,
        364,3,14,7,0,360,361,5,43,0,0,361,363,3,14,7,0,362,360,1,0,0,0,363,
        366,1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,368,1,0,0,0,366,
        364,1,0,0,0,367,359,1,0,0,0,367,368,1,0,0,0,368,369,1,0,0,0,369,
        370,5,40,0,0,370,65,1,0,0,0,371,372,3,88,44,0,372,373,5,44,0,0,373,
        374,5,18,0,0,374,375,5,37,0,0,375,376,3,14,7,0,376,377,5,38,0,0,
        377,378,5,42,0,0,378,67,1,0,0,0,379,380,3,88,44,0,380,381,5,44,0,
        0,381,382,5,19,0,0,382,383,5,37,0,0,383,384,3,34,17,0,384,385,5,
        38,0,0,385,386,5,42,0,0,386,69,1,0,0,0,387,388,3,88,44,0,388,389,
        5,44,0,0,389,390,5,21,0,0,390,391,5,37,0,0,391,392,3,34,17,0,392,
        393,5,43,0,0,393,394,3,14,7,0,394,395,5,38,0,0,395,396,5,42,0,0,
        396,71,1,0,0,0,397,398,3,10,5,0,398,399,3,88,44,0,399,400,5,37,0,
        0,400,401,3,74,37,0,401,402,5,38,0,0,402,406,5,39,0,0,403,405,3,
        2,1,0,404,403,1,0,0,0,405,408,1,0,0,0,406,404,1,0,0,0,406,407,1,
        0,0,0,407,409,1,0,0,0,408,406,1,0,0,0,409,410,3,78,39,0,410,411,
        5,40,0,0,411,427,1,0,0,0,412,413,5,22,0,0,413,414,3,88,44,0,414,
        415,5,37,0,0,415,416,3,74,37,0,416,417,5,38,0,0,417,421,5,39,0,0,
        418,420,3,2,1,0,419,418,1,0,0,0,420,423,1,0,0,0,421,419,1,0,0,0,
        421,422,1,0,0,0,422,424,1,0,0,0,423,421,1,0,0,0,424,425,5,40,0,0,
        425,427,1,0,0,0,426,397,1,0,0,0,426,412,1,0,0,0,427,73,1,0,0,0,428,
        433,3,76,38,0,429,430,5,43,0,0,430,432,3,76,38,0,431,429,1,0,0,0,
        432,435,1,0,0,0,433,431,1,0,0,0,433,434,1,0,0,0,434,437,1,0,0,0,
        435,433,1,0,0,0,436,428,1,0,0,0,436,437,1,0,0,0,437,75,1,0,0,0,438,
        439,3,10,5,0,439,440,3,88,44,0,440,77,1,0,0,0,441,442,5,17,0,0,442,
        443,3,14,7,0,443,444,5,42,0,0,444,79,1,0,0,0,445,446,7,2,0,0,446,
        81,1,0,0,0,447,452,5,46,0,0,448,452,5,47,0,0,449,452,5,48,0,0,450,
        452,3,84,42,0,451,447,1,0,0,0,451,448,1,0,0,0,451,449,1,0,0,0,451,
        450,1,0,0,0,452,83,1,0,0,0,453,454,7,3,0,0,454,85,1,0,0,0,455,456,
        7,4,0,0,456,87,1,0,0,0,457,458,5,45,0,0,458,89,1,0,0,0,33,93,109,
        129,141,155,163,170,177,185,195,205,222,225,229,240,249,253,262,
        270,279,294,303,318,329,344,364,367,406,421,426,433,436,451
    ]

class CinematographyParser ( Parser ):

    grammarFileName = "Cinematography.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'char'", "'script'", "'bool'", 
                     "'new'", "'film'", "'onScreen'", "'true'", "'false'", 
                     "'check'", "'else'", "'for'", "'do'", "'while'", "'record'", 
                     "'reel'", "'return'", "'add'", "'cut'", "'get'", "'overwrite'", 
                     "'nomemory'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'<='", "'>'", "'>='", "'=='", "'!='", "'='", "'&&'", 
                     "'||'", "'('", "')'", "'{'", "'}'", "':'", "';'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "INT", "CHAR", "SCRIPT", "BOOL", "NEW", 
                      "FILM", "ONSCREEN", "TRUE", "FALSE", "CHECK", "ELSE", 
                      "FOR", "DO", "WHILE", "RECORD", "REEL", "RETURN", 
                      "ADD", "CUT", "GET", "OVERWRITE", "NOMEMORY", "PLUS", 
                      "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "LESS", "LESS_EQUAL", 
                      "GREATER", "GREATER_EQUAL", "EQUAL", "NOT_EQUAL", 
                      "ASSIGN", "AND", "OR", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "COLON", "SEMI", "COMMA", "DOT", "IDENTIFIER", 
                      "NUMBER", "STRING", "CHARACTER", "COMMENT", "WHITESPACE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_inputStatement = 2
    RULE_outputStatement = 3
    RULE_declarationStatement = 4
    RULE_declaredType = 5
    RULE_assignmentStatement = 6
    RULE_expression = 7
    RULE_logicalOrExpression = 8
    RULE_logicalAndExpression = 9
    RULE_comparisonExpression = 10
    RULE_additiveExpression = 11
    RULE_multiplicativeExpression = 12
    RULE_operand = 13
    RULE_constructorCall = 14
    RULE_functionCall = 15
    RULE_argumentList = 16
    RULE_index = 17
    RULE_ifStatement = 18
    RULE_condition = 19
    RULE_logicalOrCondition = 20
    RULE_logicalAndCondition = 21
    RULE_conditionAtom = 22
    RULE_forStatement = 23
    RULE_forInitialization = 24
    RULE_forAssignment = 25
    RULE_whileStatement = 26
    RULE_userDatatypeStatement = 27
    RULE_field = 28
    RULE_vectorStatement = 29
    RULE_vectorCreation = 30
    RULE_vectorAssignment = 31
    RULE_vector = 32
    RULE_vectorAdd = 33
    RULE_vectorRemoveAtIndex = 34
    RULE_vectorSetAtIndex = 35
    RULE_functionStatement = 36
    RULE_parameters = 37
    RULE_parameter = 38
    RULE_returnStatement = 39
    RULE_type = 40
    RULE_value = 41
    RULE_booleanValue = 42
    RULE_relationalOperator = 43
    RULE_identifier = 44

    ruleNames =  [ "program", "statement", "inputStatement", "outputStatement", 
                   "declarationStatement", "declaredType", "assignmentStatement", 
                   "expression", "logicalOrExpression", "logicalAndExpression", 
                   "comparisonExpression", "additiveExpression", "multiplicativeExpression", 
                   "operand", "constructorCall", "functionCall", "argumentList", 
                   "index", "ifStatement", "condition", "logicalOrCondition", 
                   "logicalAndCondition", "conditionAtom", "forStatement", 
                   "forInitialization", "forAssignment", "whileStatement", 
                   "userDatatypeStatement", "field", "vectorStatement", 
                   "vectorCreation", "vectorAssignment", "vector", "vectorAdd", 
                   "vectorRemoveAtIndex", "vectorSetAtIndex", "functionStatement", 
                   "parameters", "parameter", "returnStatement", "type", 
                   "value", "booleanValue", "relationalOperator", "identifier" ]

    EOF = Token.EOF
    INT=1
    CHAR=2
    SCRIPT=3
    BOOL=4
    NEW=5
    FILM=6
    ONSCREEN=7
    TRUE=8
    FALSE=9
    CHECK=10
    ELSE=11
    FOR=12
    DO=13
    WHILE=14
    RECORD=15
    REEL=16
    RETURN=17
    ADD=18
    CUT=19
    GET=20
    OVERWRITE=21
    NOMEMORY=22
    PLUS=23
    MINUS=24
    MULTIPLY=25
    DIVIDE=26
    MODULO=27
    LESS=28
    LESS_EQUAL=29
    GREATER=30
    GREATER_EQUAL=31
    EQUAL=32
    NOT_EQUAL=33
    ASSIGN=34
    AND=35
    OR=36
    LPAREN=37
    RPAREN=38
    LBRACE=39
    RBRACE=40
    COLON=41
    SEMI=42
    COMMA=43
    DOT=44
    IDENTIFIER=45
    NUMBER=46
    STRING=47
    CHARACTER=48
    COMMENT=49
    WHITESPACE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CinematographyParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.StatementContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.StatementContext,i)


        def getRuleIndex(self):
            return CinematographyParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CinematographyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376534238) != 0):
                self.state = 90
                self.statement()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(CinematographyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputStatement(self):
            return self.getTypedRuleContext(CinematographyParser.InputStatementContext,0)


        def outputStatement(self):
            return self.getTypedRuleContext(CinematographyParser.OutputStatementContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(CinematographyParser.DeclarationStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(CinematographyParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(CinematographyParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(CinematographyParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(CinematographyParser.WhileStatementContext,0)


        def userDatatypeStatement(self):
            return self.getTypedRuleContext(CinematographyParser.UserDatatypeStatementContext,0)


        def vectorStatement(self):
            return self.getTypedRuleContext(CinematographyParser.VectorStatementContext,0)


        def functionStatement(self):
            return self.getTypedRuleContext(CinematographyParser.FunctionStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(CinematographyParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CinematographyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.inputStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.outputStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.declarationStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 105
                self.userDatatypeStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 106
                self.vectorStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 107
                self.functionStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 108
                self.returnStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILM(self):
            return self.getToken(CinematographyParser.FILM, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_inputStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = CinematographyParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(CinematographyParser.FILM)
            self.state = 112
            self.match(CinematographyParser.LPAREN)
            self.state = 113
            self.identifier()
            self.state = 114
            self.match(CinematographyParser.RPAREN)
            self.state = 115
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONSCREEN(self):
            return self.getToken(CinematographyParser.ONSCREEN, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_outputStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStatement" ):
                return visitor.visitOutputStatement(self)
            else:
                return visitor.visitChildren(self)




    def outputStatement(self):

        localctx = CinematographyParser.OutputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_outputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(CinematographyParser.ONSCREEN)
            self.state = 118
            self.match(CinematographyParser.LPAREN)
            self.state = 119
            self.expression()
            self.state = 120
            self.match(CinematographyParser.RPAREN)
            self.state = 121
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.IdentifierContext,i)


        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.COMMA)
            else:
                return self.getToken(CinematographyParser.COMMA, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_declarationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = CinematographyParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declarationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.declaredType()
            self.state = 124
            self.identifier()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 125
                self.match(CinematographyParser.COMMA)
                self.state = 126
                self.identifier()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CinematographyParser.TypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def REEL(self):
            return self.getToken(CinematographyParser.REEL, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_declaredType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaredType" ):
                return visitor.visitDeclaredType(self)
            else:
                return visitor.visitChildren(self)




    def declaredType(self):

        localctx = CinematographyParser.DeclaredTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaredType)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.type_()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.identifier()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(CinematographyParser.REEL)
                self.state = 137
                self.match(CinematographyParser.LPAREN)
                self.state = 138
                self.declaredType()
                self.state = 139
                self.match(CinematographyParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(CinematographyParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = CinematographyParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.identifier()
            self.state = 144
            self.match(CinematographyParser.ASSIGN)
            self.state = 145
            self.expression()
            self.state = 146
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(CinematographyParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CinematographyParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.LogicalAndExpressionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.OR)
            else:
                return self.getToken(CinematographyParser.OR, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_logicalOrExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = CinematographyParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.logicalAndExpression()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 151
                self.match(CinematographyParser.OR)
                self.state = 152
                self.logicalAndExpression()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.ComparisonExpressionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.ComparisonExpressionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.AND)
            else:
                return self.getToken(CinematographyParser.AND, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_logicalAndExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = CinematographyParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.comparisonExpression()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 159
                self.match(CinematographyParser.AND)
                self.state = 160
                self.comparisonExpression()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.AdditiveExpressionContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(CinematographyParser.RelationalOperatorContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_comparisonExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpression(self):

        localctx = CinematographyParser.ComparisonExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparisonExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.additiveExpression()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0):
                self.state = 167
                self.relationalOperator()
                self.state = 168
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.PLUS)
            else:
                return self.getToken(CinematographyParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.MINUS)
            else:
                return self.getToken(CinematographyParser.MINUS, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_additiveExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = CinematographyParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.multiplicativeExpression()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 174
                self.multiplicativeExpression()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.OperandContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.OperandContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.MULTIPLY)
            else:
                return self.getToken(CinematographyParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.DIVIDE)
            else:
                return self.getToken(CinematographyParser.DIVIDE, i)

        def MODULO(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.MODULO)
            else:
                return self.getToken(CinematographyParser.MODULO, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_multiplicativeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = CinematographyParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.operand()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0):
                self.state = 181
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
                self.operand()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(CinematographyParser.DOT, 0)

        def GET(self):
            return self.getToken(CinematographyParser.GET, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def index(self):
            return self.getTypedRuleContext(CinematographyParser.IndexContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def value(self):
            return self.getTypedRuleContext(CinematographyParser.ValueContext,0)


        def NEW(self):
            return self.getToken(CinematographyParser.NEW, 0)

        def constructorCall(self):
            return self.getTypedRuleContext(CinematographyParser.ConstructorCallContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(CinematographyParser.FunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = CinematographyParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.identifier()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==44:
                    self.state = 189
                    self.match(CinematographyParser.DOT)
                    self.state = 190
                    self.match(CinematographyParser.GET)
                    self.state = 191
                    self.match(CinematographyParser.LPAREN)
                    self.state = 192
                    self.index()
                    self.state = 193
                    self.match(CinematographyParser.RPAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.match(CinematographyParser.NEW)
                self.state = 199
                self.constructorCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.match(CinematographyParser.LPAREN)
                self.state = 202
                self.expression()
                self.state = 203
                self.match(CinematographyParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(CinematographyParser.ArgumentListContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_constructorCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorCall" ):
                return visitor.visitConstructorCall(self)
            else:
                return visitor.visitChildren(self)




    def constructorCall(self):

        localctx = CinematographyParser.ConstructorCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constructorCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.identifier()
            self.state = 208
            self.match(CinematographyParser.LPAREN)
            self.state = 209
            self.argumentList()
            self.state = 210
            self.match(CinematographyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(CinematographyParser.ArgumentListContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = CinematographyParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.identifier()
            self.state = 213
            self.match(CinematographyParser.LPAREN)
            self.state = 214
            self.argumentList()
            self.state = 215
            self.match(CinematographyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.COMMA)
            else:
                return self.getToken(CinematographyParser.COMMA, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = CinematographyParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 527903020286752) != 0):
                self.state = 217
                self.expression()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43:
                    self.state = 218
                    self.match(CinematographyParser.COMMA)
                    self.state = 219
                    self.expression()
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CinematographyParser.NUMBER, 0)

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = CinematographyParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_index)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(CinematographyParser.NUMBER)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHECK(self):
            return self.getToken(CinematographyParser.CHECK, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(CinematographyParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def DO(self):
            return self.getToken(CinematographyParser.DO, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.LBRACE)
            else:
                return self.getToken(CinematographyParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.RBRACE)
            else:
                return self.getToken(CinematographyParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.StatementContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(CinematographyParser.ELSE, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = CinematographyParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(CinematographyParser.CHECK)
            self.state = 232
            self.match(CinematographyParser.LPAREN)
            self.state = 233
            self.condition()
            self.state = 234
            self.match(CinematographyParser.RPAREN)
            self.state = 235
            self.match(CinematographyParser.DO)
            self.state = 236
            self.match(CinematographyParser.LBRACE)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376534238) != 0):
                self.state = 237
                self.statement()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            self.match(CinematographyParser.RBRACE)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 244
                self.match(CinematographyParser.ELSE)
                self.state = 245
                self.match(CinematographyParser.LBRACE)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376534238) != 0):
                    self.state = 246
                    self.statement()
                    self.state = 251
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 252
                self.match(CinematographyParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrCondition(self):
            return self.getTypedRuleContext(CinematographyParser.LogicalOrConditionContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = CinematographyParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.logicalOrCondition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.LogicalAndConditionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.LogicalAndConditionContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.OR)
            else:
                return self.getToken(CinematographyParser.OR, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_logicalOrCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrCondition" ):
                return visitor.visitLogicalOrCondition(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrCondition(self):

        localctx = CinematographyParser.LogicalOrConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicalOrCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.logicalAndCondition()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 258
                self.match(CinematographyParser.OR)
                self.state = 259
                self.logicalAndCondition()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.ConditionAtomContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.ConditionAtomContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.AND)
            else:
                return self.getToken(CinematographyParser.AND, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_logicalAndCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndCondition" ):
                return visitor.visitLogicalAndCondition(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndCondition(self):

        localctx = CinematographyParser.LogicalAndConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicalAndCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.conditionAtom()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 266
                self.match(CinematographyParser.AND)
                self.state = 267
                self.conditionAtom()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpression(self):
            return self.getTypedRuleContext(CinematographyParser.ComparisonExpressionContext,0)


        def booleanValue(self):
            return self.getTypedRuleContext(CinematographyParser.BooleanValueContext,0)


        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(CinematographyParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_conditionAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionAtom" ):
                return visitor.visitConditionAtom(self)
            else:
                return visitor.visitChildren(self)




    def conditionAtom(self):

        localctx = CinematographyParser.ConditionAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_conditionAtom)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.comparisonExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.booleanValue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(CinematographyParser.LPAREN)
                self.state = 276
                self.condition()
                self.state = 277
                self.match(CinematographyParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CinematographyParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def forInitialization(self):
            return self.getTypedRuleContext(CinematographyParser.ForInitializationContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.SEMI)
            else:
                return self.getToken(CinematographyParser.SEMI, i)

        def condition(self):
            return self.getTypedRuleContext(CinematographyParser.ConditionContext,0)


        def forAssignment(self):
            return self.getTypedRuleContext(CinematographyParser.ForAssignmentContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def DO(self):
            return self.getToken(CinematographyParser.DO, 0)

        def LBRACE(self):
            return self.getToken(CinematographyParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CinematographyParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.StatementContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.StatementContext,i)


        def getRuleIndex(self):
            return CinematographyParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = CinematographyParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(CinematographyParser.FOR)
            self.state = 282
            self.match(CinematographyParser.LPAREN)
            self.state = 283
            self.forInitialization()
            self.state = 284
            self.match(CinematographyParser.SEMI)
            self.state = 285
            self.condition()
            self.state = 286
            self.match(CinematographyParser.SEMI)
            self.state = 287
            self.forAssignment()
            self.state = 288
            self.match(CinematographyParser.RPAREN)
            self.state = 289
            self.match(CinematographyParser.DO)
            self.state = 290
            self.match(CinematographyParser.LBRACE)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376534238) != 0):
                self.state = 291
                self.statement()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 297
            self.match(CinematographyParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def forAssignment(self):
            return self.getTypedRuleContext(CinematographyParser.ForAssignmentContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_forInitialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitialization" ):
                return visitor.visitForInitialization(self)
            else:
                return visitor.visitChildren(self)




    def forInitialization(self):

        localctx = CinematographyParser.ForInitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forInitialization)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.declaredType()
                self.state = 300
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.forAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(CinematographyParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_forAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForAssignment" ):
                return visitor.visitForAssignment(self)
            else:
                return visitor.visitChildren(self)




    def forAssignment(self):

        localctx = CinematographyParser.ForAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.identifier()
            self.state = 306
            self.match(CinematographyParser.ASSIGN)
            self.state = 307
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CinematographyParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(CinematographyParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def DO(self):
            return self.getToken(CinematographyParser.DO, 0)

        def LBRACE(self):
            return self.getToken(CinematographyParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CinematographyParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.StatementContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.StatementContext,i)


        def getRuleIndex(self):
            return CinematographyParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = CinematographyParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(CinematographyParser.WHILE)
            self.state = 310
            self.match(CinematographyParser.LPAREN)
            self.state = 311
            self.condition()
            self.state = 312
            self.match(CinematographyParser.RPAREN)
            self.state = 313
            self.match(CinematographyParser.DO)
            self.state = 314
            self.match(CinematographyParser.LBRACE)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376534238) != 0):
                self.state = 315
                self.statement()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 321
            self.match(CinematographyParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UserDatatypeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self):
            return self.getToken(CinematographyParser.RECORD, 0)

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def LBRACE(self):
            return self.getToken(CinematographyParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CinematographyParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.FieldContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.FieldContext,i)


        def getRuleIndex(self):
            return CinematographyParser.RULE_userDatatypeStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUserDatatypeStatement" ):
                return visitor.visitUserDatatypeStatement(self)
            else:
                return visitor.visitChildren(self)




    def userDatatypeStatement(self):

        localctx = CinematographyParser.UserDatatypeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_userDatatypeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(CinematographyParser.RECORD)
            self.state = 324
            self.identifier()
            self.state = 325
            self.match(CinematographyParser.LBRACE)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372154398) != 0):
                self.state = 326
                self.field()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 332
            self.match(CinematographyParser.RBRACE)
            self.state = 333
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = CinematographyParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.declaredType()
            self.state = 336
            self.identifier()
            self.state = 337
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vectorCreation(self):
            return self.getTypedRuleContext(CinematographyParser.VectorCreationContext,0)


        def vectorAssignment(self):
            return self.getTypedRuleContext(CinematographyParser.VectorAssignmentContext,0)


        def vectorAdd(self):
            return self.getTypedRuleContext(CinematographyParser.VectorAddContext,0)


        def vectorRemoveAtIndex(self):
            return self.getTypedRuleContext(CinematographyParser.VectorRemoveAtIndexContext,0)


        def vectorSetAtIndex(self):
            return self.getTypedRuleContext(CinematographyParser.VectorSetAtIndexContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_vectorStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorStatement" ):
                return visitor.visitVectorStatement(self)
            else:
                return visitor.visitChildren(self)




    def vectorStatement(self):

        localctx = CinematographyParser.VectorStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_vectorStatement)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.vectorCreation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.vectorAssignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.vectorAdd()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.vectorRemoveAtIndex()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 343
                self.vectorSetAtIndex()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorCreationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REEL(self):
            return self.getToken(CinematographyParser.REEL, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_vectorCreation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorCreation" ):
                return visitor.visitVectorCreation(self)
            else:
                return visitor.visitChildren(self)




    def vectorCreation(self):

        localctx = CinematographyParser.VectorCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_vectorCreation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(CinematographyParser.REEL)
            self.state = 347
            self.match(CinematographyParser.LPAREN)
            self.state = 348
            self.declaredType()
            self.state = 349
            self.match(CinematographyParser.RPAREN)
            self.state = 350
            self.identifier()
            self.state = 351
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(CinematographyParser.ASSIGN, 0)

        def vector(self):
            return self.getTypedRuleContext(CinematographyParser.VectorContext,0)


        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_vectorAssignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorAssignment" ):
                return visitor.visitVectorAssignment(self)
            else:
                return visitor.visitChildren(self)




    def vectorAssignment(self):

        localctx = CinematographyParser.VectorAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_vectorAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.identifier()
            self.state = 354
            self.match(CinematographyParser.ASSIGN)
            self.state = 355
            self.vector()
            self.state = 356
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CinematographyParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CinematographyParser.RBRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.COMMA)
            else:
                return self.getToken(CinematographyParser.COMMA, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_vector

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector" ):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)




    def vector(self):

        localctx = CinematographyParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_vector)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(CinematographyParser.LBRACE)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 527903020286752) != 0):
                self.state = 359
                self.expression()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43:
                    self.state = 360
                    self.match(CinematographyParser.COMMA)
                    self.state = 361
                    self.expression()
                    self.state = 366
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 369
            self.match(CinematographyParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorAddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(CinematographyParser.DOT, 0)

        def ADD(self):
            return self.getToken(CinematographyParser.ADD, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_vectorAdd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorAdd" ):
                return visitor.visitVectorAdd(self)
            else:
                return visitor.visitChildren(self)




    def vectorAdd(self):

        localctx = CinematographyParser.VectorAddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_vectorAdd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.identifier()
            self.state = 372
            self.match(CinematographyParser.DOT)
            self.state = 373
            self.match(CinematographyParser.ADD)
            self.state = 374
            self.match(CinematographyParser.LPAREN)
            self.state = 375
            self.expression()
            self.state = 376
            self.match(CinematographyParser.RPAREN)
            self.state = 377
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorRemoveAtIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(CinematographyParser.DOT, 0)

        def CUT(self):
            return self.getToken(CinematographyParser.CUT, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def index(self):
            return self.getTypedRuleContext(CinematographyParser.IndexContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_vectorRemoveAtIndex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorRemoveAtIndex" ):
                return visitor.visitVectorRemoveAtIndex(self)
            else:
                return visitor.visitChildren(self)




    def vectorRemoveAtIndex(self):

        localctx = CinematographyParser.VectorRemoveAtIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_vectorRemoveAtIndex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.identifier()
            self.state = 380
            self.match(CinematographyParser.DOT)
            self.state = 381
            self.match(CinematographyParser.CUT)
            self.state = 382
            self.match(CinematographyParser.LPAREN)
            self.state = 383
            self.index()
            self.state = 384
            self.match(CinematographyParser.RPAREN)
            self.state = 385
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorSetAtIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(CinematographyParser.DOT, 0)

        def OVERWRITE(self):
            return self.getToken(CinematographyParser.OVERWRITE, 0)

        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def index(self):
            return self.getTypedRuleContext(CinematographyParser.IndexContext,0)


        def COMMA(self):
            return self.getToken(CinematographyParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_vectorSetAtIndex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorSetAtIndex" ):
                return visitor.visitVectorSetAtIndex(self)
            else:
                return visitor.visitChildren(self)




    def vectorSetAtIndex(self):

        localctx = CinematographyParser.VectorSetAtIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_vectorSetAtIndex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.identifier()
            self.state = 388
            self.match(CinematographyParser.DOT)
            self.state = 389
            self.match(CinematographyParser.OVERWRITE)
            self.state = 390
            self.match(CinematographyParser.LPAREN)
            self.state = 391
            self.index()
            self.state = 392
            self.match(CinematographyParser.COMMA)
            self.state = 393
            self.expression()
            self.state = 394
            self.match(CinematographyParser.RPAREN)
            self.state = 395
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(CinematographyParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(CinematographyParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(CinematographyParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CinematographyParser.LBRACE, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(CinematographyParser.ReturnStatementContext,0)


        def RBRACE(self):
            return self.getToken(CinematographyParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.StatementContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.StatementContext,i)


        def NOMEMORY(self):
            return self.getToken(CinematographyParser.NOMEMORY, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_functionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionStatement" ):
                return visitor.visitFunctionStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionStatement(self):

        localctx = CinematographyParser.FunctionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_functionStatement)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 16, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.declaredType()
                self.state = 398
                self.identifier()
                self.state = 399
                self.match(CinematographyParser.LPAREN)
                self.state = 400
                self.parameters()
                self.state = 401
                self.match(CinematographyParser.RPAREN)
                self.state = 402
                self.match(CinematographyParser.LBRACE)
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 403
                        self.statement() 
                    self.state = 408
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 409
                self.returnStatement()
                self.state = 410
                self.match(CinematographyParser.RBRACE)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(CinematographyParser.NOMEMORY)
                self.state = 413
                self.identifier()
                self.state = 414
                self.match(CinematographyParser.LPAREN)
                self.state = 415
                self.parameters()
                self.state = 416
                self.match(CinematographyParser.RPAREN)
                self.state = 417
                self.match(CinematographyParser.LBRACE)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376534238) != 0):
                    self.state = 418
                    self.statement()
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424
                self.match(CinematographyParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CinematographyParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CinematographyParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CinematographyParser.COMMA)
            else:
                return self.getToken(CinematographyParser.COMMA, i)

        def getRuleIndex(self):
            return CinematographyParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = CinematographyParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372154398) != 0):
                self.state = 428
                self.parameter()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43:
                    self.state = 429
                    self.match(CinematographyParser.COMMA)
                    self.state = 430
                    self.parameter()
                    self.state = 435
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredType(self):
            return self.getTypedRuleContext(CinematographyParser.DeclaredTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CinematographyParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = CinematographyParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.declaredType()
            self.state = 439
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CinematographyParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(CinematographyParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CinematographyParser.SEMI, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = CinematographyParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(CinematographyParser.RETURN)
            self.state = 442
            self.expression()
            self.state = 443
            self.match(CinematographyParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CinematographyParser.INT, 0)

        def CHAR(self):
            return self.getToken(CinematographyParser.CHAR, 0)

        def SCRIPT(self):
            return self.getToken(CinematographyParser.SCRIPT, 0)

        def BOOL(self):
            return self.getToken(CinematographyParser.BOOL, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CinematographyParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CinematographyParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(CinematographyParser.STRING, 0)

        def CHARACTER(self):
            return self.getToken(CinematographyParser.CHARACTER, 0)

        def booleanValue(self):
            return self.getTypedRuleContext(CinematographyParser.BooleanValueContext,0)


        def getRuleIndex(self):
            return CinematographyParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CinematographyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_value)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(CinematographyParser.NUMBER)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(CinematographyParser.STRING)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.match(CinematographyParser.CHARACTER)
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 450
                self.booleanValue()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CinematographyParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CinematographyParser.FALSE, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_booleanValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanValue" ):
                return visitor.visitBooleanValue(self)
            else:
                return visitor.visitChildren(self)




    def booleanValue(self):

        localctx = CinematographyParser.BooleanValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_booleanValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(CinematographyParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(CinematographyParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(CinematographyParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(CinematographyParser.GREATER_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(CinematographyParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CinematographyParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_relationalOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOperator" ):
                return visitor.visitRelationalOperator(self)
            else:
                return visitor.visitChildren(self)




    def relationalOperator(self):

        localctx = CinematographyParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CinematographyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CinematographyParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = CinematographyParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(CinematographyParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





