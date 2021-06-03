# QuickNote

## alias `python main.py` to `qnote` by:  
`alias qnote="python main.py"` if you consider using it only in your script directory.  
`alias qnote='cd /your/path/to/script/directory; python main.py'` if you want to use it from anywhere.  

to permanently store your alias:  
if you are using **zsh** then:  
`echo -e "\nalias qnote='cd /path/to/your/script/directory; python main.py'" >> ~/.zshrc`  
or if you need to specify python3  
`echo -e "\nalias qnote='cd /path/to/your/script/directory; python3 main.py'" >> ~/.zshrc`  

## Commands list:  
[date] = [[yyyy-mm-dd], today, tomorrow]  
`qnote help`  
`qnote -a [date] "note message"`    
`qnote [date]`    

## Flags
If no flags specified, script will retrieve notes for specified date `[date]`.  
`-a` flag adds new notes to a particular date.  
When `-a` flag is used `"note message"` should be passed after `[date]`.

## Usage sample.  

`qnote tomorrow`
>$ qnote tomorrow  
>Nothing found for tomorrow  

`qnote -a tomorrow "buy milk"`
>$ qnote -a tomorrow "buy milk"  
buy milk added to tomorrow  


`qnote tomorrow`
>$ qn tomorrow  
Planned for tomorrow:  
        buy milk  
