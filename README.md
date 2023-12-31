## Ticker symbol parsing and convention conversions.

## Install
`pip install symbol_parser`   

#### All functionality is accessed through the Symbol class.
```python
from symbol_parser import Symbol
```
see [symbol.py](./symbol_parser/symbol.py) for usage.   

## Data
Data used in this module is extracted from https://www.nasdaqtrader.com/Trader.aspx?id=CQSSymbolConvention
<table>
    <tbody>
        <tr>
            <th><strong>Security<br>
            Categorization</strong></th>
            <th><strong>CQS Suffix</strong></th>
            <th><strong>CMS Suffix</strong></th>
            <th><strong>NASDAQ Integrated Platform Suffix</strong></th>
            <th>NASDAQ ACT/CTCI Suffixes</th>
        </tr>
       <tr><td>Preferred</td><td>p</td><td>PR</td><td>-</td><td>$</td></tr>
        <tr><td>Preferred Class "A"*</td><td>pA</td><td>PRA</td><td>-A</td><td>&nbsp;$A</td></tr>
        <tr><td>Preferred Class "B"*</td><td>pB</td><td>PRB</td><td>-B</td><td>$B</td></tr>
        <tr><td>Class "A"*</td><td>.A</td><td>A</td><td>.A</td><td>&nbsp;.A</td></tr>
        <tr><td>Class "B"*</td><td>.B</td><td>B</td><td>.B</td><td>&nbsp; .B</td></tr>
        <tr><td>Preferred when distributed</td><td>p.WD</td><td>PRWD</td><td>-$</td><td>.D</td></tr>
        <tr><td>When distributed</td><td>.WD</td><td>WD</td><td>$</td><td>.Z</td></tr>
        <tr><td>Warrants</td><td>.WS</td><td>WS</td><td>+</td><td>.W</td></tr>
        <tr><td>Warrants Class "A"*</td><td>.WS.A</td><td>WSA</td><td>+A</td><td>.W or .A**</td></tr>
        <tr><td>Warrants Class "B"*</td><td>.WS.B</td><td>WSB</td><td>+B</td><td>&nbsp;</td></tr>
        <tr><td>Called</td><td>.CL</td><td>CL</td><td>*</td><td>&nbsp;</td></tr>
        <tr><td>Class "A" Called*</td><td>.A.CL</td><td>ACL</td><td>.A*</td><td>.A</td></tr>
        <tr><td>Preferred called</td><td>p.CL</td><td>PRCL</td><td>-*</td><td>$</td></tr>
        <tr><td>Preferred "A" called*</td><td>pA.CL</td><td>PRACL</td><td>-A*</td><td>$A</td></tr>
        <tr><td>Preferred "A" when issued*</td><td>pAw</td><td>PRAWI</td><td>-A#</td><td>&nbsp;.V or .Z</td></tr>
        <tr><td>Emerging Company Marketplace</td><td>.EC</td><td>EC</td><td>!</td><td>.E</td></tr>
        <tr><td>Partial Paid</td><td>.PP</td><td>PP</td><td>@</td><td>&nbsp;</td></tr>
        <tr><td>Convertible</td><td>.CV</td><td>CV</td><td>%</td><td>&nbsp;</td></tr>
        <tr><td>Convertible called</td><td>.CV.CL</td><td>CVCL</td><td>%*</td><td>&nbsp;</td></tr>
        <tr><td>Class Convertible</td><td>.A.CV</td><td>ACV</td><td>.A%</td><td>&nbsp;</td></tr>
        <tr><td>Preferred (class A) Convertible</td><td>pA.CV</td><td>PRACV</td><td>-A%</td><td>&nbsp;</td></tr>
        <tr><td>Preferred (class A) when Distributed</td><td>pA.WD</td><td>PRAWD</td><td>-A$</td><td>&nbsp;</td></tr>
        <tr><td>Rights</td><td>r</td><td>RT</td><td>^</td><td>.R</td></tr>
        <tr><td>Units</td><td>.U</td><td>U</td><td>=</td><td>.U</td></tr>
        <tr><td>When issued</td><td>w</td><td>WI</td><td>#</td><td>.V or .Z</td></tr>
        <tr><td>Rights when issued</td><td>rw</td><td>RTWI</td><td>^#</td><td>.V or .Z</td></tr>
        <tr><td>Preferred when issued</td><td>pw</td><td>PRWI</td><td>-#</td><td>.V or .Z</td></tr>
        <tr><td>Class "A" when issued*</td><td>.Aw</td><td>AWI</td><td>.A#</td><td>.V or .Z</td></tr>
        <tr><td>Warrrant when issued</td><td>.WSw</td><td>WSWI</td><td>+#</td><td>.V or .Z</td></tr>
        <tr><td>TEST symbol</td><td>.TEST</td><td>TEST</td><td>~</td><td></td></tr>
    </tbody>
</table>
