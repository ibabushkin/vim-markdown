" functions to insert and modify timestamps in markdown documents
" formatted according to *THE RULES*

" we need python for our calculations
if !has('python')
	finish
endif

" insert a timestamp with Day, Month and Year
function! InsertTimestamp(desc, mode)
        python import sys
        python sys.argv = [] 
	pyfile ~/.vim/ftplugin/markdown/insert_timestamp.py
endfunc

" bind to a command
command! -nargs=+ InsertTimestamp call InsertTimestamp(<f-args>)

" insert a timestamp with Day, Month, Year, Hour and Minute
function! InsertExactTimestamp(desc, time, mode)
        python import sys
        python sys.argv = ["exact"] 
        pyfile insert_timestamp.py
endfunc

" bind to a command
command! -nargs=+ InsertTimestampExact call InsertExactTimestamp(<f-args>)

