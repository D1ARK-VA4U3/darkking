o
    τb  γ                	   @   sΐ  d dl mZ d dlmZ d dlZd dlZd dlmZmZ d dl	m
Z
 e  ejZejZejZejZejZejZejZeeeeeegZzd dlZW n ey_   ee de  e d‘ Y nw dd	 Zd
d Z	 e  e  eed e  eed e  eed e  eed e  eed e  e e!dZ"e"dkr'g Z#e$ddoZ%e e!de de Z&e'e&D ]!Z(e)e!de de Z*d +e* ,‘ ‘Z-e .e-ge%‘ e# /e-‘ qΊede d e  ede d e#D ]Z0ede0 ddZ1e1 2e0‘ ee d e1 3‘  qρe!d  W d   n	1 sw   Y  e% 4‘  n8e"d!kr
g Z5g Z6e$dd"Z7	 z
e5 /e 8e7‘‘ W n
 e9yJ   Y nw q6e7 4‘  e:e5d krdeed#  e
d$ nϋe5D ]LZ;e)e;d  Z<ede< d%d&Z=e= >‘  e= ?‘ s±ze= @e<‘ eeA d'e< d(e  W qf ey°   eee)e< d) e  e6 /e;‘ Y qfw qfe:e6d krΖeed*  e!d+ ne6D ]ZBe5 CeB‘ qΘe$dd,ZDe5D ]Z"e"d  ZEe .eEgeD‘ qΩW d   n	1 sσw   Y  eD 4‘  eed- e  e!d+ nUe"d$kr«g ZFe$dd"ZG	 z
eF /e 8eG‘‘ W n
 e9y+   Y nw qeG 4‘  d Z(ee d. eFD ]ZHee d/e( d0eHd   e  e(d7 Z(q=e e!de d1e ZIe)eFeI d  Z<e<d2 ZJejKd3kr|e d4eJ ‘ ne d5eJ ‘ eFeI= e$dd,ZGeFD ]	Z;e .e;eG‘ qede d6e  e!d+ eG 4‘  n΄e"d7krQede d8 ze Ld9‘ZMW n   ee d: ee d; eN  Y eOeMjPd<krEe)e!e d=eMjP d>e ZQeQd?ksϋeQd@ksϋeQdAkr9ee dB ejKd3kre dC‘ e dD‘ n
e dE‘ e dF‘ e dG‘ e dH‘ ee dIeMjP  e!dJ eN  n&ee dK e!dL nee dM e!dL ne"dNkr_e  e  eN  qi)Oι    )ΪTelegramClient)ΪPhoneNumberBannedErrorN)ΪinitΪFore)Ϊsleepz#[i] Installing module - requests...zpip install requestsc                  C   sH   dd l } g d’}|D ]}t|  t‘ | t  q
tdt d d S )Nr   )uJ    ββββββββββββββββββββββββ uJ    ββββββββββββββββββββββββ uJ    ββββββββββββββββββββββββ uJ    ββββββββββββββββββββββββ uJ    ββββββββββββββββββββββββ uJ    ββββββββββββββββββββββββ z   Version: 1.0 | Author: REXΪ
)ΪrandomΪprintΪchoiceΪcolorsΪn)r   ΪbΪchar© r   ϊ%/storage/emulated/0/gjk/rexmanager.pyΪbanner   s
   r   c                   C   s&   t jdkrt  d‘ d S t  d‘ d S )NΪntΪclsΪclear)ΪosΪnameΪsystemr   r   r   r   Ϊclr+   s   
r   Tz[1] Add New Accountsz[2] Filter All Banned Accountsz[3] Delete specific accountsz[4] Update your Scriptz[5] Exitz
Enter Your Choice: ι   zvars.txtΪabr   z& [~] Enter number of accounts to add: z [~] Enter Phone Number: Ϊ z# [i] Saved all accounts in vars.txtz" [*] Logging in from new accounts
z	sessions/i$ Z 7e14b38d250953c8c1e94fd7b2d63550u>   [+] ππ¨π π’π§ π¬π?ππππ¬π¬ππ?Lz"
 Press enter to goto main menu...ι   Ϊrbz4[!] There are no accounts! Please add some and retryι   il{ Z 7d1e0295ee1c2628f1933e9ffd2d8b78z[+] z is not bannedz is banned!zCongrats! No banned accountsz!
Press enter to goto main menu...Ϊwbz[i] All banned accounts removedz [i] Choose an account to delete
ϊ[z] z[+] Enter a choice: z.sessionr   zdel sessions\zrm sessions/z[+] Account Deletedι   z[i] Checking for updates...zOhttps://raw.githubusercontent.com/krish775/Rex-TG-Member-Adder/main/version.txtz& You are not connected to the internetz) Please connect to the internet and retrygΝΜΜΜΜΜμ?z[~] Update available[Version z]. Download?[y/n]: ΪyZyesΪYz[i] Downloading updates...zdel rexadder.pyzdel rexmanager.pyzrm rexadder.pyzrm rexmanager.pyzZcurl -l -O https://raw.githubusercontent.com/krish775/Rex-TG-Member-Adder/main/rexadder.pyz\curl -l -O https://raw.githubusercontent.com/krish775/Rex-TG-Member-Adder/main/rexmanager.pyz[*] Updated to version: zPress enter to exit...z[!] Update aborted.z Press enter to goto main menu...z$[i] Your Astra is already up to dateι   )RZtelethon.syncr   Ztelethon.errors.rpcerrorlistr   Ϊpickler   Zcoloramar   r   Ϊtimer   ZRESETr   ZBLUEZlgZREDΪrZWHITEΪwZCYANΪcyZYELLOWZyeZGREENZgrr   ZrequestsΪImportErrorr	   r   r   r   ΪintΪinputΪaZnew_accsΪopenΪgZnumber_to_addΪrangeΪiΪstrZphone_numberΪjoinΪsplitZparsed_numberΪdumpΪappendZnumberΪcΪstartZ
disconnectΪcloseZaccountsZbanned_accsΪhΪloadΪEOFErrorΪlenZaccountZphoneZclientZconnectZis_user_authorizedZsend_code_requestZblueΪmΪremoveΪkZPhoneZaccsΪfZaccΪindexZsession_filer   ΪgetΪversionΪexitΪfloatΪtextΪpromptr   r   r   r   Ϊ<module>   s4   ώ



ρ

?ύ

ώϋώ?

?ύ 










 ϋ