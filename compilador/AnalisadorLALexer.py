# Generated from compilador/AnalisadorLA.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,65,523,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,
        1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,
        1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,
        1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,
        1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,
        1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,55,
        1,55,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,58,1,59,4,59,466,
        8,59,11,59,12,59,467,1,60,4,60,471,8,60,11,60,12,60,472,1,60,1,60,
        4,60,477,8,60,11,60,12,60,478,3,60,481,8,60,1,61,1,61,5,61,485,8,
        61,10,61,12,61,488,9,61,1,62,1,62,1,62,5,62,493,8,62,10,62,12,62,
        496,9,62,1,62,1,62,1,63,1,63,1,63,1,63,3,63,504,8,63,1,64,1,64,5,
        64,508,8,64,10,64,12,64,511,9,64,1,64,3,64,514,8,64,1,64,1,64,1,
        64,1,64,1,65,1,65,1,65,1,65,0,0,66,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,
        121,61,123,62,125,63,127,0,129,64,131,65,1,0,5,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,3,0,10,10,34,34,92,92,3,0,10,10,
        13,13,125,125,3,0,9,10,13,13,32,32,531,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,
        1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,
        1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,
        1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,
        1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,
        1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,
        1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,
        1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,
        1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,
        1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,
        105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,
        0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,
        1,0,0,0,0,125,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,1,133,1,0,0,0,
        3,143,1,0,0,0,5,157,1,0,0,0,7,165,1,0,0,0,9,175,1,0,0,0,11,177,1,
        0,0,0,13,179,1,0,0,0,15,184,1,0,0,0,17,186,1,0,0,0,19,188,1,0,0,
        0,21,190,1,0,0,0,23,192,1,0,0,0,25,200,1,0,0,0,27,208,1,0,0,0,29,
        213,1,0,0,0,31,220,1,0,0,0,33,222,1,0,0,0,35,233,1,0,0,0,37,239,
        1,0,0,0,39,248,1,0,0,0,41,261,1,0,0,0,43,274,1,0,0,0,45,276,1,0,
        0,0,47,278,1,0,0,0,49,295,1,0,0,0,51,302,1,0,0,0,53,313,1,0,0,0,
        55,317,1,0,0,0,57,322,1,0,0,0,59,330,1,0,0,0,61,333,1,0,0,0,63,339,
        1,0,0,0,65,346,1,0,0,0,67,352,1,0,0,0,69,357,1,0,0,0,71,362,1,0,
        0,0,73,371,1,0,0,0,75,376,1,0,0,0,77,379,1,0,0,0,79,383,1,0,0,0,
        81,388,1,0,0,0,83,397,1,0,0,0,85,406,1,0,0,0,87,419,1,0,0,0,89,427,
        1,0,0,0,91,430,1,0,0,0,93,432,1,0,0,0,95,434,1,0,0,0,97,436,1,0,
        0,0,99,438,1,0,0,0,101,440,1,0,0,0,103,442,1,0,0,0,105,445,1,0,0,
        0,107,448,1,0,0,0,109,451,1,0,0,0,111,453,1,0,0,0,113,455,1,0,0,
        0,115,459,1,0,0,0,117,462,1,0,0,0,119,465,1,0,0,0,121,470,1,0,0,
        0,123,482,1,0,0,0,125,489,1,0,0,0,127,503,1,0,0,0,129,505,1,0,0,
        0,131,519,1,0,0,0,133,134,5,97,0,0,134,135,5,108,0,0,135,136,5,103,
        0,0,136,137,5,111,0,0,137,138,5,114,0,0,138,139,5,105,0,0,139,140,
        5,116,0,0,140,141,5,109,0,0,141,142,5,111,0,0,142,2,1,0,0,0,143,
        144,5,102,0,0,144,145,5,105,0,0,145,146,5,109,0,0,146,147,5,95,0,
        0,147,148,5,97,0,0,148,149,5,108,0,0,149,150,5,103,0,0,150,151,5,
        111,0,0,151,152,5,114,0,0,152,153,5,105,0,0,153,154,5,116,0,0,154,
        155,5,109,0,0,155,156,5,111,0,0,156,4,1,0,0,0,157,158,5,100,0,0,
        158,159,5,101,0,0,159,160,5,99,0,0,160,161,5,108,0,0,161,162,5,97,
        0,0,162,163,5,114,0,0,163,164,5,101,0,0,164,6,1,0,0,0,165,166,5,
        99,0,0,166,167,5,111,0,0,167,168,5,110,0,0,168,169,5,115,0,0,169,
        170,5,116,0,0,170,171,5,97,0,0,171,172,5,110,0,0,172,173,5,116,0,
        0,173,174,5,101,0,0,174,8,1,0,0,0,175,176,5,58,0,0,176,10,1,0,0,
        0,177,178,5,61,0,0,178,12,1,0,0,0,179,180,5,116,0,0,180,181,5,105,
        0,0,181,182,5,112,0,0,182,183,5,111,0,0,183,14,1,0,0,0,184,185,5,
        44,0,0,185,16,1,0,0,0,186,187,5,46,0,0,187,18,1,0,0,0,188,189,5,
        91,0,0,189,20,1,0,0,0,190,191,5,93,0,0,191,22,1,0,0,0,192,193,5,
        108,0,0,193,194,5,105,0,0,194,195,5,116,0,0,195,196,5,101,0,0,196,
        197,5,114,0,0,197,198,5,97,0,0,198,199,5,108,0,0,199,24,1,0,0,0,
        200,201,5,105,0,0,201,202,5,110,0,0,202,203,5,116,0,0,203,204,5,
        101,0,0,204,205,5,105,0,0,205,206,5,114,0,0,206,207,5,111,0,0,207,
        26,1,0,0,0,208,209,5,114,0,0,209,210,5,101,0,0,210,211,5,97,0,0,
        211,212,5,108,0,0,212,28,1,0,0,0,213,214,5,108,0,0,214,215,5,111,
        0,0,215,216,5,103,0,0,216,217,5,105,0,0,217,218,5,99,0,0,218,219,
        5,111,0,0,219,30,1,0,0,0,220,221,5,94,0,0,221,32,1,0,0,0,222,223,
        5,118,0,0,223,224,5,101,0,0,224,225,5,114,0,0,225,226,5,100,0,0,
        226,227,5,97,0,0,227,228,5,100,0,0,228,229,5,101,0,0,229,230,5,105,
        0,0,230,231,5,114,0,0,231,232,5,111,0,0,232,34,1,0,0,0,233,234,5,
        102,0,0,234,235,5,97,0,0,235,236,5,108,0,0,236,237,5,115,0,0,237,
        238,5,111,0,0,238,36,1,0,0,0,239,240,5,114,0,0,240,241,5,101,0,0,
        241,242,5,103,0,0,242,243,5,105,0,0,243,244,5,115,0,0,244,245,5,
        116,0,0,245,246,5,114,0,0,246,247,5,111,0,0,247,38,1,0,0,0,248,249,
        5,102,0,0,249,250,5,105,0,0,250,251,5,109,0,0,251,252,5,95,0,0,252,
        253,5,114,0,0,253,254,5,101,0,0,254,255,5,103,0,0,255,256,5,105,
        0,0,256,257,5,115,0,0,257,258,5,116,0,0,258,259,5,114,0,0,259,260,
        5,111,0,0,260,40,1,0,0,0,261,262,5,112,0,0,262,263,5,114,0,0,263,
        264,5,111,0,0,264,265,5,99,0,0,265,266,5,101,0,0,266,267,5,100,0,
        0,267,268,5,105,0,0,268,269,5,109,0,0,269,270,5,101,0,0,270,271,
        5,110,0,0,271,272,5,116,0,0,272,273,5,111,0,0,273,42,1,0,0,0,274,
        275,5,40,0,0,275,44,1,0,0,0,276,277,5,41,0,0,277,46,1,0,0,0,278,
        279,5,102,0,0,279,280,5,105,0,0,280,281,5,109,0,0,281,282,5,95,0,
        0,282,283,5,112,0,0,283,284,5,114,0,0,284,285,5,111,0,0,285,286,
        5,99,0,0,286,287,5,101,0,0,287,288,5,100,0,0,288,289,5,105,0,0,289,
        290,5,109,0,0,290,291,5,101,0,0,291,292,5,110,0,0,292,293,5,116,
        0,0,293,294,5,111,0,0,294,48,1,0,0,0,295,296,5,102,0,0,296,297,5,
        117,0,0,297,298,5,110,0,0,298,299,5,99,0,0,299,300,5,97,0,0,300,
        301,5,111,0,0,301,50,1,0,0,0,302,303,5,102,0,0,303,304,5,105,0,0,
        304,305,5,109,0,0,305,306,5,95,0,0,306,307,5,102,0,0,307,308,5,117,
        0,0,308,309,5,110,0,0,309,310,5,99,0,0,310,311,5,97,0,0,311,312,
        5,111,0,0,312,52,1,0,0,0,313,314,5,118,0,0,314,315,5,97,0,0,315,
        316,5,114,0,0,316,54,1,0,0,0,317,318,5,108,0,0,318,319,5,101,0,0,
        319,320,5,105,0,0,320,321,5,97,0,0,321,56,1,0,0,0,322,323,5,101,
        0,0,323,324,5,115,0,0,324,325,5,99,0,0,325,326,5,114,0,0,326,327,
        5,101,0,0,327,328,5,118,0,0,328,329,5,97,0,0,329,58,1,0,0,0,330,
        331,5,115,0,0,331,332,5,101,0,0,332,60,1,0,0,0,333,334,5,101,0,0,
        334,335,5,110,0,0,335,336,5,116,0,0,336,337,5,97,0,0,337,338,5,111,
        0,0,338,62,1,0,0,0,339,340,5,102,0,0,340,341,5,105,0,0,341,342,5,
        109,0,0,342,343,5,95,0,0,343,344,5,115,0,0,344,345,5,101,0,0,345,
        64,1,0,0,0,346,347,5,115,0,0,347,348,5,101,0,0,348,349,5,110,0,0,
        349,350,5,97,0,0,350,351,5,111,0,0,351,66,1,0,0,0,352,353,5,99,0,
        0,353,354,5,97,0,0,354,355,5,115,0,0,355,356,5,111,0,0,356,68,1,
        0,0,0,357,358,5,115,0,0,358,359,5,101,0,0,359,360,5,106,0,0,360,
        361,5,97,0,0,361,70,1,0,0,0,362,363,5,102,0,0,363,364,5,105,0,0,
        364,365,5,109,0,0,365,366,5,95,0,0,366,367,5,99,0,0,367,368,5,97,
        0,0,368,369,5,115,0,0,369,370,5,111,0,0,370,72,1,0,0,0,371,372,5,
        112,0,0,372,373,5,97,0,0,373,374,5,114,0,0,374,375,5,97,0,0,375,
        74,1,0,0,0,376,377,5,60,0,0,377,378,5,45,0,0,378,76,1,0,0,0,379,
        380,5,97,0,0,380,381,5,116,0,0,381,382,5,101,0,0,382,78,1,0,0,0,
        383,384,5,102,0,0,384,385,5,97,0,0,385,386,5,99,0,0,386,387,5,97,
        0,0,387,80,1,0,0,0,388,389,5,102,0,0,389,390,5,105,0,0,390,391,5,
        109,0,0,391,392,5,95,0,0,392,393,5,112,0,0,393,394,5,97,0,0,394,
        395,5,114,0,0,395,396,5,97,0,0,396,82,1,0,0,0,397,398,5,101,0,0,
        398,399,5,110,0,0,399,400,5,113,0,0,400,401,5,117,0,0,401,402,5,
        97,0,0,402,403,5,110,0,0,403,404,5,116,0,0,404,405,5,111,0,0,405,
        84,1,0,0,0,406,407,5,102,0,0,407,408,5,105,0,0,408,409,5,109,0,0,
        409,410,5,95,0,0,410,411,5,101,0,0,411,412,5,110,0,0,412,413,5,113,
        0,0,413,414,5,117,0,0,414,415,5,97,0,0,415,416,5,110,0,0,416,417,
        5,116,0,0,417,418,5,111,0,0,418,86,1,0,0,0,419,420,5,114,0,0,420,
        421,5,101,0,0,421,422,5,116,0,0,422,423,5,111,0,0,423,424,5,114,
        0,0,424,425,5,110,0,0,425,426,5,101,0,0,426,88,1,0,0,0,427,428,5,
        46,0,0,428,429,5,46,0,0,429,90,1,0,0,0,430,431,5,45,0,0,431,92,1,
        0,0,0,432,433,5,43,0,0,433,94,1,0,0,0,434,435,5,42,0,0,435,96,1,
        0,0,0,436,437,5,47,0,0,437,98,1,0,0,0,438,439,5,37,0,0,439,100,1,
        0,0,0,440,441,5,38,0,0,441,102,1,0,0,0,442,443,5,60,0,0,443,444,
        5,62,0,0,444,104,1,0,0,0,445,446,5,62,0,0,446,447,5,61,0,0,447,106,
        1,0,0,0,448,449,5,60,0,0,449,450,5,61,0,0,450,108,1,0,0,0,451,452,
        5,62,0,0,452,110,1,0,0,0,453,454,5,60,0,0,454,112,1,0,0,0,455,456,
        5,110,0,0,456,457,5,97,0,0,457,458,5,111,0,0,458,114,1,0,0,0,459,
        460,5,111,0,0,460,461,5,117,0,0,461,116,1,0,0,0,462,463,5,101,0,
        0,463,118,1,0,0,0,464,466,2,48,57,0,465,464,1,0,0,0,466,467,1,0,
        0,0,467,465,1,0,0,0,467,468,1,0,0,0,468,120,1,0,0,0,469,471,2,48,
        57,0,470,469,1,0,0,0,471,472,1,0,0,0,472,470,1,0,0,0,472,473,1,0,
        0,0,473,480,1,0,0,0,474,476,5,46,0,0,475,477,2,48,57,0,476,475,1,
        0,0,0,477,478,1,0,0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,481,1,
        0,0,0,480,474,1,0,0,0,480,481,1,0,0,0,481,122,1,0,0,0,482,486,7,
        0,0,0,483,485,7,1,0,0,484,483,1,0,0,0,485,488,1,0,0,0,486,484,1,
        0,0,0,486,487,1,0,0,0,487,124,1,0,0,0,488,486,1,0,0,0,489,494,5,
        34,0,0,490,493,3,127,63,0,491,493,8,2,0,0,492,490,1,0,0,0,492,491,
        1,0,0,0,493,496,1,0,0,0,494,492,1,0,0,0,494,495,1,0,0,0,495,497,
        1,0,0,0,496,494,1,0,0,0,497,498,5,34,0,0,498,126,1,0,0,0,499,500,
        5,92,0,0,500,504,5,34,0,0,501,502,5,92,0,0,502,504,5,110,0,0,503,
        499,1,0,0,0,503,501,1,0,0,0,504,128,1,0,0,0,505,509,5,123,0,0,506,
        508,8,3,0,0,507,506,1,0,0,0,508,511,1,0,0,0,509,507,1,0,0,0,509,
        510,1,0,0,0,510,513,1,0,0,0,511,509,1,0,0,0,512,514,5,13,0,0,513,
        512,1,0,0,0,513,514,1,0,0,0,514,515,1,0,0,0,515,516,5,125,0,0,516,
        517,1,0,0,0,517,518,6,64,0,0,518,130,1,0,0,0,519,520,7,4,0,0,520,
        521,1,0,0,0,521,522,6,65,0,0,522,132,1,0,0,0,11,0,467,472,478,480,
        486,492,494,503,509,513,1,6,0,0
    ]

class AnalisadorLALexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    NUM_INT = 60
    NUM_REAL = 61
    IDENT = 62
    CADEIA = 63
    COMENTARIO = 64
    WS = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'algoritmo'", "'fim_algoritmo'", "'declare'", "'constante'", 
            "':'", "'='", "'tipo'", "','", "'.'", "'['", "']'", "'literal'", 
            "'inteiro'", "'real'", "'logico'", "'^'", "'verdadeiro'", "'falso'", 
            "'registro'", "'fim_registro'", "'procedimento'", "'('", "')'", 
            "'fim_procedimento'", "'funcao'", "'fim_funcao'", "'var'", "'leia'", 
            "'escreva'", "'se'", "'entao'", "'fim_se'", "'senao'", "'caso'", 
            "'seja'", "'fim_caso'", "'para'", "'<-'", "'ate'", "'faca'", 
            "'fim_para'", "'enquanto'", "'fim_enquanto'", "'retorne'", "'..'", 
            "'-'", "'+'", "'*'", "'/'", "'%'", "'&'", "'<>'", "'>='", "'<='", 
            "'>'", "'<'", "'nao'", "'ou'", "'e'" ]

    symbolicNames = [ "<INVALID>",
            "NUM_INT", "NUM_REAL", "IDENT", "CADEIA", "COMENTARIO", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "NUM_INT", "NUM_REAL", "IDENT", 
                  "CADEIA", "ESC_SEQ", "COMENTARIO", "WS" ]

    grammarFileName = "AnalisadorLA.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


