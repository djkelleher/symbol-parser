import re

suffix_regs = {
    'Preferred': re.compile(r'((?P<cqs>p$)|(?P<cms>\ PR$)|(?P<nasdaq_ip>\-$)|(?P<act_ctci>\$$))'),
    'Preferred Class "A"*': re.compile(r'((?P<cqs>pA$)|(?P<cms>\ PRA$)|(?P<nasdaq_ip>\-A$)|(?P<act_ctci>\$A$))'),
    'Preferred Class "B"*': re.compile(r'((?P<cqs>pB$)|(?P<cms>\ PRB$)|(?P<nasdaq_ip>\-B$)|(?P<act_ctci>\$B$))'),
    'Class "A"*': re.compile(r'((?P<cqs>\.A$)|(?P<cms>\ A$)|(?P<nasdaq_ip>\.A$)|(?P<act_ctci>\.A$))'),
    'Class "B"*': re.compile(r'((?P<cqs>\.B$)|(?P<cms>\ B$)|(?P<nasdaq_ip>\.B$)|(?P<act_ctci>\.B$))'),
    'Preferred when distributed': re.compile(r'((?P<cqs>p\.WD$)|(?P<cms>\ PRWD$)|(?P<nasdaq_ip>\-\$$)|(?P<act_ctci>\.D$))'),
    'When distributed': re.compile(r'((?P<cqs>\.WD$)|(?P<cms>\ WD$)|(?P<nasdaq_ip>\$$)|(?P<act_ctci>\.Z$))'),
    'Warrants': re.compile(r'((?P<cqs>\.WS$)|(?P<cms>\ WS$)|(?P<nasdaq_ip>\+$)|(?P<act_ctci>\.W$))'),
    'Warrants Class "A"*': re.compile(r'((?P<cqs>\.WS\.A$)|(?P<cms>\ WSA$)|(?P<nasdaq_ip>\+A$)|(?P<act_ctci>(\.W$|\.A\*\*$)))'),
    'Warrants Class "B"*': re.compile(r'((?P<cqs>\.WS\.B$)|(?P<cms>\ WSB$)|(?P<nasdaq_ip>\+B$))'),
    'Called': re.compile(r'((?P<cqs>\.CL$)|(?P<cms>\ CL$)|(?P<nasdaq_ip>\*$))'),
    'Class "A" Called*': re.compile(r'((?P<cqs>\.A\.CL$)|(?P<cms>\ ACL$)|(?P<nasdaq_ip>\.A\*$)|(?P<act_ctci>\.A$))'),
    'Preferred called': re.compile(r'((?P<cqs>p\.CL$)|(?P<cms>\ PRCL$)|(?P<nasdaq_ip>\-\*$)|(?P<act_ctci>\$$))'),
    'Preferred "A" called*': re.compile(r'((?P<cqs>pA\.CL$)|(?P<cms>\ PRACL$)|(?P<nasdaq_ip>\-A\*$)|(?P<act_ctci>\$A$))'),
    'Preferred "A" when issued*': re.compile(r'((?P<cqs>pAw$)|(?P<cms>\ PRAWI$)|(?P<nasdaq_ip>\-A\#$)|(?P<act_ctci>(\.V$|\.Z$)))'),
    'Emerging Company Marketplace': re.compile(r'((?P<cqs>\.EC$)|(?P<cms>\ EC$)|(?P<nasdaq_ip>!$)|(?P<act_ctci>\.E$))'),
    'Partial Paid': re.compile(r'((?P<cqs>\.PP$)|(?P<cms>\ PP$)|(?P<nasdaq_ip>@$))'),
    'Convertible': re.compile(r'((?P<cqs>\.CV$)|(?P<cms>\ CV$)|(?P<nasdaq_ip>%$))'),
    'Convertible called': re.compile(r'((?P<cqs>\.CV\.CL$)|(?P<cms>\ CVCL$)|(?P<nasdaq_ip>%\*$))'),
    'Class Convertible': re.compile(r'((?P<cqs>\.A\.CV$)|(?P<cms>\ ACV$)|(?P<nasdaq_ip>\.A%$))'),
    'Preferred (class A) Convertible': re.compile(r'((?P<cqs>pA\.CV$)|(?P<cms>\ PRACV$)|(?P<nasdaq_ip>\-A%$))'),
    'Preferred (class A) when Distributed': re.compile(r'((?P<cqs>pA\.WD$)|(?P<cms>\ PRAWD$)|(?P<nasdaq_ip>\-A\$$))'),
    'Rights': re.compile(r'((?P<cqs>r$)|(?P<cms>\ RT$)|(?P<nasdaq_ip>\^$)|(?P<act_ctci>\.R$))'),
    'Units': re.compile(r'((?P<cqs>\.U$)|(?P<cms>\ U$)|(?P<nasdaq_ip>=$)|(?P<act_ctci>\.U$))'),
    'When issued': re.compile(r'((?P<cqs>w$)|(?P<cms>\ WI$)|(?P<nasdaq_ip>\#$)|(?P<act_ctci>(\.V$|\.Z$)))'),
    'Rights when issued': re.compile(r'((?P<cqs>rw$)|(?P<cms>\ RTWI$)|(?P<nasdaq_ip>\^\#$)|(?P<act_ctci>(\.V$|\.Z$)))'),
    'Preferred when issued': re.compile(r'((?P<cqs>pw$)|(?P<cms>\ PRWI$)|(?P<nasdaq_ip>\-\#$)|(?P<act_ctci>(\.V$|\.Z$)))'),
    'Class "A" when issued*': re.compile(r'((?P<cqs>\.Aw$)|(?P<cms>\ AWI$)|(?P<nasdaq_ip>\.A\#$)|(?P<act_ctci>(\.V$|\.Z$)))'),
    'Warrrant when issued': re.compile(r'((?P<cqs>\.WSw$)|(?P<cms>\ WSWI$)|(?P<nasdaq_ip>\+\#$)|(?P<act_ctci>(\.V$|\.Z$)))'),
    'TEST symbol': re.compile(r'((?P<cqs>\.TEST$)|(?P<cms>\ TEST$)|(?P<nasdaq_ip>\~$))')
}