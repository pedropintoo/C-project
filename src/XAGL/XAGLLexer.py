# Generated from XAGLLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,89,657,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,
        1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,39,
        1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,43,
        1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,47,
        1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,
        1,50,1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,52,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,54,1,54,
        1,54,1,55,1,55,1,55,1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,
        1,58,1,58,1,58,1,59,1,59,1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,
        1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,63,1,63,1,63,1,64,1,64,1,64,
        1,64,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,67,1,67,1,68,1,68,
        1,69,1,69,1,70,1,70,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,
        1,74,1,74,1,75,1,75,1,75,1,76,1,76,1,76,1,76,1,77,1,77,1,77,1,78,
        1,78,1,78,1,78,1,79,1,79,1,79,1,79,1,79,1,79,1,79,1,79,1,79,3,79,
        564,8,79,1,80,1,80,1,80,5,80,569,8,80,10,80,12,80,572,9,80,1,81,
        1,81,1,82,4,82,577,8,82,11,82,12,82,578,1,83,4,83,582,8,83,11,83,
        12,83,583,1,83,1,83,4,83,588,8,83,11,83,12,83,589,1,83,1,83,3,83,
        594,8,83,1,83,4,83,597,8,83,11,83,12,83,598,3,83,601,8,83,1,84,1,
        84,1,84,5,84,606,8,84,10,84,12,84,609,9,84,1,84,1,84,1,85,1,85,1,
        86,1,86,1,87,1,87,1,87,1,87,3,87,621,8,87,1,88,1,88,5,88,625,8,88,
        10,88,12,88,628,9,88,1,88,1,88,1,88,1,88,1,89,1,89,1,89,1,89,1,89,
        5,89,639,8,89,10,89,12,89,642,9,89,1,89,1,89,1,89,1,89,1,89,1,90,
        4,90,650,8,90,11,90,12,90,651,1,90,1,90,1,91,1,91,3,607,626,640,
        0,92,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,
        35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,
        46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,
        56,113,57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,
        131,66,133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,
        75,151,76,153,77,155,78,157,79,159,80,161,81,163,82,165,83,167,84,
        169,85,171,0,173,0,175,0,177,86,179,87,181,88,183,89,1,0,6,1,0,46,
        46,2,0,69,69,101,101,2,0,43,43,45,45,4,0,65,90,95,95,97,122,192,
        255,1,0,48,57,3,0,9,10,13,13,32,32,669,0,1,1,0,0,0,0,3,1,0,0,0,0,
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
        1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,
        0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,
        0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,
        151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,
        0,0,0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,
        1,0,0,0,0,177,1,0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,
        1,185,1,0,0,0,3,187,1,0,0,0,5,189,1,0,0,0,7,191,1,0,0,0,9,193,1,
        0,0,0,11,195,1,0,0,0,13,197,1,0,0,0,15,199,1,0,0,0,17,201,1,0,0,
        0,19,203,1,0,0,0,21,205,1,0,0,0,23,208,1,0,0,0,25,210,1,0,0,0,27,
        213,1,0,0,0,29,221,1,0,0,0,31,228,1,0,0,0,33,235,1,0,0,0,35,241,
        1,0,0,0,37,248,1,0,0,0,39,253,1,0,0,0,41,261,1,0,0,0,43,266,1,0,
        0,0,45,271,1,0,0,0,47,281,1,0,0,0,49,289,1,0,0,0,51,293,1,0,0,0,
        53,302,1,0,0,0,55,311,1,0,0,0,57,316,1,0,0,0,59,320,1,0,0,0,61,329,
        1,0,0,0,63,336,1,0,0,0,65,344,1,0,0,0,67,349,1,0,0,0,69,355,1,0,
        0,0,71,360,1,0,0,0,73,366,1,0,0,0,75,373,1,0,0,0,77,378,1,0,0,0,
        79,381,1,0,0,0,81,387,1,0,0,0,83,395,1,0,0,0,85,401,1,0,0,0,87,407,
        1,0,0,0,89,413,1,0,0,0,91,418,1,0,0,0,93,427,1,0,0,0,95,433,1,0,
        0,0,97,438,1,0,0,0,99,443,1,0,0,0,101,447,1,0,0,0,103,453,1,0,0,
        0,105,460,1,0,0,0,107,466,1,0,0,0,109,469,1,0,0,0,111,474,1,0,0,
        0,113,477,1,0,0,0,115,480,1,0,0,0,117,486,1,0,0,0,119,489,1,0,0,
        0,121,491,1,0,0,0,123,496,1,0,0,0,125,503,1,0,0,0,127,506,1,0,0,
        0,129,509,1,0,0,0,131,516,1,0,0,0,133,519,1,0,0,0,135,521,1,0,0,
        0,137,523,1,0,0,0,139,525,1,0,0,0,141,527,1,0,0,0,143,529,1,0,0,
        0,145,531,1,0,0,0,147,534,1,0,0,0,149,537,1,0,0,0,151,540,1,0,0,
        0,153,543,1,0,0,0,155,547,1,0,0,0,157,550,1,0,0,0,159,563,1,0,0,
        0,161,565,1,0,0,0,163,573,1,0,0,0,165,576,1,0,0,0,167,581,1,0,0,
        0,169,602,1,0,0,0,171,612,1,0,0,0,173,614,1,0,0,0,175,620,1,0,0,
        0,177,622,1,0,0,0,179,633,1,0,0,0,181,649,1,0,0,0,183,655,1,0,0,
        0,185,186,5,40,0,0,186,2,1,0,0,0,187,188,5,41,0,0,188,4,1,0,0,0,
        189,190,5,123,0,0,190,6,1,0,0,0,191,192,5,125,0,0,192,8,1,0,0,0,
        193,194,5,91,0,0,194,10,1,0,0,0,195,196,5,93,0,0,196,12,1,0,0,0,
        197,198,5,58,0,0,198,14,1,0,0,0,199,200,5,61,0,0,200,16,1,0,0,0,
        201,202,5,59,0,0,202,18,1,0,0,0,203,204,5,44,0,0,204,20,1,0,0,0,
        205,206,5,46,0,0,206,207,5,46,0,0,207,22,1,0,0,0,208,209,5,46,0,
        0,209,24,1,0,0,0,210,211,5,58,0,0,211,212,5,58,0,0,212,26,1,0,0,
        0,213,214,5,73,0,0,214,215,5,110,0,0,215,216,5,116,0,0,216,217,5,
        101,0,0,217,218,5,103,0,0,218,219,5,101,0,0,219,220,5,114,0,0,220,
        28,1,0,0,0,221,222,5,78,0,0,222,223,5,117,0,0,223,224,5,109,0,0,
        224,225,5,98,0,0,225,226,5,101,0,0,226,227,5,114,0,0,227,30,1,0,
        0,0,228,229,5,83,0,0,229,230,5,116,0,0,230,231,5,114,0,0,231,232,
        5,105,0,0,232,233,5,110,0,0,233,234,5,103,0,0,234,32,1,0,0,0,235,
        236,5,80,0,0,236,237,5,111,0,0,237,238,5,105,0,0,238,239,5,110,0,
        0,239,240,5,116,0,0,240,34,1,0,0,0,241,242,5,86,0,0,242,243,5,101,
        0,0,243,244,5,99,0,0,244,245,5,116,0,0,245,246,5,111,0,0,246,247,
        5,114,0,0,247,36,1,0,0,0,248,249,5,84,0,0,249,250,5,105,0,0,250,
        251,5,109,0,0,251,252,5,101,0,0,252,38,1,0,0,0,253,254,5,66,0,0,
        254,255,5,111,0,0,255,256,5,111,0,0,256,257,5,108,0,0,257,258,5,
        101,0,0,258,259,5,97,0,0,259,260,5,110,0,0,260,40,1,0,0,0,261,262,
        5,86,0,0,262,263,5,105,0,0,263,264,5,101,0,0,264,265,5,119,0,0,265,
        42,1,0,0,0,266,267,5,76,0,0,267,268,5,105,0,0,268,269,5,110,0,0,
        269,270,5,101,0,0,270,44,1,0,0,0,271,272,5,82,0,0,272,273,5,101,
        0,0,273,274,5,99,0,0,274,275,5,116,0,0,275,276,5,97,0,0,276,277,
        5,110,0,0,277,278,5,103,0,0,278,279,5,108,0,0,279,280,5,101,0,0,
        280,46,1,0,0,0,281,282,5,69,0,0,282,283,5,108,0,0,283,284,5,108,
        0,0,284,285,5,105,0,0,285,286,5,112,0,0,286,287,5,115,0,0,287,288,
        5,101,0,0,288,48,1,0,0,0,289,290,5,65,0,0,290,291,5,114,0,0,291,
        292,5,99,0,0,292,50,1,0,0,0,293,294,5,65,0,0,294,295,5,114,0,0,295,
        296,5,99,0,0,296,297,5,67,0,0,297,298,5,104,0,0,298,299,5,111,0,
        0,299,300,5,114,0,0,300,301,5,100,0,0,301,52,1,0,0,0,302,303,5,80,
        0,0,303,304,5,105,0,0,304,305,5,101,0,0,305,306,5,83,0,0,306,307,
        5,108,0,0,307,308,5,105,0,0,308,309,5,99,0,0,309,310,5,101,0,0,310,
        54,1,0,0,0,311,312,5,84,0,0,312,313,5,101,0,0,313,314,5,120,0,0,
        314,315,5,116,0,0,315,56,1,0,0,0,316,317,5,68,0,0,317,318,5,111,
        0,0,318,319,5,116,0,0,319,58,1,0,0,0,320,321,5,80,0,0,321,322,5,
        111,0,0,322,323,5,108,0,0,323,324,5,121,0,0,324,325,5,76,0,0,325,
        326,5,105,0,0,326,327,5,110,0,0,327,328,5,101,0,0,328,60,1,0,0,0,
        329,330,5,83,0,0,330,331,5,112,0,0,331,332,5,108,0,0,332,333,5,105,
        0,0,333,334,5,110,0,0,334,335,5,101,0,0,335,62,1,0,0,0,336,337,5,
        80,0,0,337,338,5,111,0,0,338,339,5,108,0,0,339,340,5,121,0,0,340,
        341,5,103,0,0,341,342,5,111,0,0,342,343,5,110,0,0,343,64,1,0,0,0,
        344,345,5,66,0,0,345,346,5,108,0,0,346,347,5,111,0,0,347,348,5,98,
        0,0,348,66,1,0,0,0,349,350,5,77,0,0,350,351,5,111,0,0,351,352,5,
        100,0,0,352,353,5,101,0,0,353,354,5,108,0,0,354,68,1,0,0,0,355,356,
        5,69,0,0,356,357,5,110,0,0,357,358,5,117,0,0,358,359,5,109,0,0,359,
        70,1,0,0,0,360,361,5,65,0,0,361,362,5,114,0,0,362,363,5,114,0,0,
        363,364,5,97,0,0,364,365,5,121,0,0,365,72,1,0,0,0,366,367,5,83,0,
        0,367,368,5,99,0,0,368,369,5,114,0,0,369,370,5,105,0,0,370,371,5,
        112,0,0,371,372,5,116,0,0,372,74,1,0,0,0,373,374,5,119,0,0,374,375,
        5,105,0,0,375,376,5,116,0,0,376,377,5,104,0,0,377,76,1,0,0,0,378,
        379,5,97,0,0,379,380,5,116,0,0,380,78,1,0,0,0,381,382,5,112,0,0,
        382,383,5,114,0,0,383,384,5,105,0,0,384,385,5,110,0,0,385,386,5,
        116,0,0,386,80,1,0,0,0,387,388,5,114,0,0,388,389,5,101,0,0,389,390,
        5,102,0,0,390,391,5,114,0,0,391,392,5,101,0,0,392,393,5,115,0,0,
        393,394,5,104,0,0,394,82,1,0,0,0,395,396,5,99,0,0,396,397,5,108,
        0,0,397,398,5,111,0,0,398,399,5,115,0,0,399,400,5,101,0,0,400,84,
        1,0,0,0,401,402,5,109,0,0,402,403,5,111,0,0,403,404,5,117,0,0,404,
        405,5,115,0,0,405,406,5,101,0,0,406,86,1,0,0,0,407,408,5,99,0,0,
        408,409,5,108,0,0,409,410,5,105,0,0,410,411,5,99,0,0,411,412,5,107,
        0,0,412,88,1,0,0,0,413,414,5,119,0,0,414,415,5,97,0,0,415,416,5,
        105,0,0,416,417,5,116,0,0,417,90,1,0,0,0,418,419,5,100,0,0,419,420,
        5,101,0,0,420,421,5,101,0,0,421,422,5,112,0,0,422,423,5,99,0,0,423,
        424,5,111,0,0,424,425,5,112,0,0,425,426,5,121,0,0,426,92,1,0,0,0,
        427,428,5,105,0,0,428,429,5,110,0,0,429,430,5,112,0,0,430,431,5,
        117,0,0,431,432,5,116,0,0,432,94,1,0,0,0,433,434,5,108,0,0,434,435,
        5,111,0,0,435,436,5,97,0,0,436,437,5,100,0,0,437,96,1,0,0,0,438,
        439,5,112,0,0,439,440,5,108,0,0,440,441,5,97,0,0,441,442,5,121,0,
        0,442,98,1,0,0,0,443,444,5,102,0,0,444,445,5,111,0,0,445,446,5,114,
        0,0,446,100,1,0,0,0,447,448,5,119,0,0,448,449,5,104,0,0,449,450,
        5,105,0,0,450,451,5,108,0,0,451,452,5,101,0,0,452,102,1,0,0,0,453,
        454,5,114,0,0,454,455,5,101,0,0,455,456,5,112,0,0,456,457,5,101,
        0,0,457,458,5,97,0,0,458,459,5,116,0,0,459,104,1,0,0,0,460,461,5,
        117,0,0,461,462,5,110,0,0,462,463,5,116,0,0,463,464,5,105,0,0,464,
        465,5,108,0,0,465,106,1,0,0,0,466,467,5,105,0,0,467,468,5,102,0,
        0,468,108,1,0,0,0,469,470,5,101,0,0,470,471,5,108,0,0,471,472,5,
        115,0,0,472,473,5,101,0,0,473,110,1,0,0,0,474,475,5,105,0,0,475,
        476,5,110,0,0,476,112,1,0,0,0,477,478,5,100,0,0,478,479,5,111,0,
        0,479,114,1,0,0,0,480,481,5,97,0,0,481,482,5,102,0,0,482,483,5,116,
        0,0,483,484,5,101,0,0,484,485,5,114,0,0,485,116,1,0,0,0,486,487,
        5,109,0,0,487,488,5,115,0,0,488,118,1,0,0,0,489,490,5,115,0,0,490,
        120,1,0,0,0,491,492,5,109,0,0,492,493,5,111,0,0,493,494,5,118,0,
        0,494,495,5,101,0,0,495,122,1,0,0,0,496,497,5,114,0,0,497,498,5,
        111,0,0,498,499,5,116,0,0,499,500,5,97,0,0,500,501,5,116,0,0,501,
        502,5,101,0,0,502,124,1,0,0,0,503,504,5,98,0,0,504,505,5,121,0,0,
        505,126,1,0,0,0,506,507,5,116,0,0,507,508,5,111,0,0,508,128,1,0,
        0,0,509,510,5,97,0,0,510,511,5,99,0,0,511,512,5,116,0,0,512,513,
        5,105,0,0,513,514,5,111,0,0,514,515,5,110,0,0,515,130,1,0,0,0,516,
        517,5,111,0,0,517,518,5,110,0,0,518,132,1,0,0,0,519,520,5,43,0,0,
        520,134,1,0,0,0,521,522,5,45,0,0,522,136,1,0,0,0,523,524,5,42,0,
        0,524,138,1,0,0,0,525,526,5,47,0,0,526,140,1,0,0,0,527,528,5,62,
        0,0,528,142,1,0,0,0,529,530,5,60,0,0,530,144,1,0,0,0,531,532,5,62,
        0,0,532,533,5,61,0,0,533,146,1,0,0,0,534,535,5,60,0,0,535,536,5,
        61,0,0,536,148,1,0,0,0,537,538,5,61,0,0,538,539,5,61,0,0,539,150,
        1,0,0,0,540,541,5,33,0,0,541,542,5,61,0,0,542,152,1,0,0,0,543,544,
        5,97,0,0,544,545,5,110,0,0,545,546,5,100,0,0,546,154,1,0,0,0,547,
        548,5,111,0,0,548,549,5,114,0,0,549,156,1,0,0,0,550,551,5,110,0,
        0,551,552,5,111,0,0,552,553,5,116,0,0,553,158,1,0,0,0,554,555,5,
        84,0,0,555,556,5,114,0,0,556,557,5,117,0,0,557,564,5,101,0,0,558,
        559,5,70,0,0,559,560,5,97,0,0,560,561,5,108,0,0,561,562,5,115,0,
        0,562,564,5,101,0,0,563,554,1,0,0,0,563,558,1,0,0,0,564,160,1,0,
        0,0,565,570,3,171,85,0,566,569,3,171,85,0,567,569,3,173,86,0,568,
        566,1,0,0,0,568,567,1,0,0,0,569,572,1,0,0,0,570,568,1,0,0,0,570,
        571,1,0,0,0,571,162,1,0,0,0,572,570,1,0,0,0,573,574,3,161,80,0,574,
        164,1,0,0,0,575,577,3,173,86,0,576,575,1,0,0,0,577,578,1,0,0,0,578,
        576,1,0,0,0,578,579,1,0,0,0,579,166,1,0,0,0,580,582,3,173,86,0,581,
        580,1,0,0,0,582,583,1,0,0,0,583,581,1,0,0,0,583,584,1,0,0,0,584,
        585,1,0,0,0,585,587,7,0,0,0,586,588,3,173,86,0,587,586,1,0,0,0,588,
        589,1,0,0,0,589,587,1,0,0,0,589,590,1,0,0,0,590,600,1,0,0,0,591,
        593,7,1,0,0,592,594,7,2,0,0,593,592,1,0,0,0,593,594,1,0,0,0,594,
        596,1,0,0,0,595,597,3,173,86,0,596,595,1,0,0,0,597,598,1,0,0,0,598,
        596,1,0,0,0,598,599,1,0,0,0,599,601,1,0,0,0,600,591,1,0,0,0,600,
        601,1,0,0,0,601,168,1,0,0,0,602,607,5,34,0,0,603,606,3,175,87,0,
        604,606,9,0,0,0,605,603,1,0,0,0,605,604,1,0,0,0,606,609,1,0,0,0,
        607,608,1,0,0,0,607,605,1,0,0,0,608,610,1,0,0,0,609,607,1,0,0,0,
        610,611,5,34,0,0,611,170,1,0,0,0,612,613,7,3,0,0,613,172,1,0,0,0,
        614,615,7,4,0,0,615,174,1,0,0,0,616,617,5,92,0,0,617,621,5,34,0,
        0,618,619,5,92,0,0,619,621,5,92,0,0,620,616,1,0,0,0,620,618,1,0,
        0,0,621,176,1,0,0,0,622,626,5,35,0,0,623,625,9,0,0,0,624,623,1,0,
        0,0,625,628,1,0,0,0,626,627,1,0,0,0,626,624,1,0,0,0,627,629,1,0,
        0,0,628,626,1,0,0,0,629,630,5,10,0,0,630,631,1,0,0,0,631,632,6,88,
        0,0,632,178,1,0,0,0,633,634,5,35,0,0,634,635,5,40,0,0,635,640,1,
        0,0,0,636,639,3,179,89,0,637,639,9,0,0,0,638,636,1,0,0,0,638,637,
        1,0,0,0,639,642,1,0,0,0,640,641,1,0,0,0,640,638,1,0,0,0,641,643,
        1,0,0,0,642,640,1,0,0,0,643,644,5,35,0,0,644,645,5,41,0,0,645,646,
        1,0,0,0,646,647,6,89,0,0,647,180,1,0,0,0,648,650,7,5,0,0,649,648,
        1,0,0,0,650,651,1,0,0,0,651,649,1,0,0,0,651,652,1,0,0,0,652,653,
        1,0,0,0,653,654,6,90,0,0,654,182,1,0,0,0,655,656,9,0,0,0,656,184,
        1,0,0,0,17,0,563,568,570,578,583,589,593,598,600,605,607,620,626,
        638,640,651,1,6,0,0
    ]

class XAGLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    LBRACE = 3
    RBRACE = 4
    LBRACK = 5
    RBRACK = 6
    COLON = 7
    EQUAL = 8
    SEMI = 9
    COMMA = 10
    TWODOTS = 11
    DOT = 12
    DOUBLECOLON = 13
    INTEGER = 14
    NUMBER = 15
    STRING_ = 16
    POINT = 17
    VECTOR = 18
    TIME = 19
    BOOLEAN_ = 20
    VIEW = 21
    LINE = 22
    RECTANGLE = 23
    ELLIPSE = 24
    ARC = 25
    ARCHORD = 26
    PIESLICE = 27
    TEXT = 28
    DOTTYPE = 29
    POLYLINE = 30
    SPLINE = 31
    POLYGON = 32
    BLOB = 33
    Model = 34
    Enum = 35
    ARRAY = 36
    SCRIPT = 37
    WITH = 38
    AT = 39
    PRINT = 40
    REFRESH = 41
    CLOSE = 42
    MOUSE = 43
    CLICK = 44
    WAIT = 45
    DEEPCOPY = 46
    INPUT = 47
    LOAD = 48
    PLAY = 49
    FOR = 50
    WHILE = 51
    REPEAT = 52
    UNTIL = 53
    IF = 54
    ELSE = 55
    IN = 56
    DO = 57
    AFTER = 58
    MS = 59
    S = 60
    MOVE = 61
    ROTATE = 62
    BY = 63
    TO = 64
    ACTION = 65
    ON = 66
    PLUS = 67
    MINUS = 68
    MUL = 69
    DIV = 70
    GT = 71
    LT = 72
    GTE = 73
    LTE = 74
    EQ = 75
    NEQ = 76
    AND = 77
    OR = 78
    NOT = 79
    BOOLEAN = 80
    ID = 81
    NAME = 82
    INT = 83
    FLOAT = 84
    STRING = 85
    LINE_COMMENT = 86
    COMMENT = 87
    WS = 88
    ERROR = 89

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", "'='", "';'", 
            "','", "'..'", "'.'", "'::'", "'Integer'", "'Number'", "'String'", 
            "'Point'", "'Vector'", "'Time'", "'Boolean'", "'View'", "'Line'", 
            "'Rectangle'", "'Ellipse'", "'Arc'", "'ArcChord'", "'PieSlice'", 
            "'Text'", "'Dot'", "'PolyLine'", "'Spline'", "'Polygon'", "'Blob'", 
            "'Model'", "'Enum'", "'Array'", "'Script'", "'with'", "'at'", 
            "'print'", "'refresh'", "'close'", "'mouse'", "'click'", "'wait'", 
            "'deepcopy'", "'input'", "'load'", "'play'", "'for'", "'while'", 
            "'repeat'", "'until'", "'if'", "'else'", "'in'", "'do'", "'after'", 
            "'ms'", "'s'", "'move'", "'rotate'", "'by'", "'to'", "'action'", 
            "'on'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'>='", "'<='", 
            "'=='", "'!='", "'and'", "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "COLON", "EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "DOUBLECOLON", 
            "INTEGER", "NUMBER", "STRING_", "POINT", "VECTOR", "TIME", "BOOLEAN_", 
            "VIEW", "LINE", "RECTANGLE", "ELLIPSE", "ARC", "ARCHORD", "PIESLICE", 
            "TEXT", "DOTTYPE", "POLYLINE", "SPLINE", "POLYGON", "BLOB", 
            "Model", "Enum", "ARRAY", "SCRIPT", "WITH", "AT", "PRINT", "REFRESH", 
            "CLOSE", "MOUSE", "CLICK", "WAIT", "DEEPCOPY", "INPUT", "LOAD", 
            "PLAY", "FOR", "WHILE", "REPEAT", "UNTIL", "IF", "ELSE", "IN", 
            "DO", "AFTER", "MS", "S", "MOVE", "ROTATE", "BY", "TO", "ACTION", 
            "ON", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "GTE", "LTE", 
            "EQ", "NEQ", "AND", "OR", "NOT", "BOOLEAN", "ID", "NAME", "INT", 
            "FLOAT", "STRING", "LINE_COMMENT", "COMMENT", "WS", "ERROR" ]

    ruleNames = [ "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                  "COLON", "EQUAL", "SEMI", "COMMA", "TWODOTS", "DOT", "DOUBLECOLON", 
                  "INTEGER", "NUMBER", "STRING_", "POINT", "VECTOR", "TIME", 
                  "BOOLEAN_", "VIEW", "LINE", "RECTANGLE", "ELLIPSE", "ARC", 
                  "ARCHORD", "PIESLICE", "TEXT", "DOTTYPE", "POLYLINE", 
                  "SPLINE", "POLYGON", "BLOB", "Model", "Enum", "ARRAY", 
                  "SCRIPT", "WITH", "AT", "PRINT", "REFRESH", "CLOSE", "MOUSE", 
                  "CLICK", "WAIT", "DEEPCOPY", "INPUT", "LOAD", "PLAY", 
                  "FOR", "WHILE", "REPEAT", "UNTIL", "IF", "ELSE", "IN", 
                  "DO", "AFTER", "MS", "S", "MOVE", "ROTATE", "BY", "TO", 
                  "ACTION", "ON", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", 
                  "GTE", "LTE", "EQ", "NEQ", "AND", "OR", "NOT", "BOOLEAN", 
                  "ID", "NAME", "INT", "FLOAT", "STRING", "LETTER", "DIGIT", 
                  "ESC", "LINE_COMMENT", "COMMENT", "WS", "ERROR" ]

    grammarFileName = "XAGLLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


