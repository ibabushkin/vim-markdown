
function! MarkdownFolds()
  let currentline = getline(v:lnum)
  if match(currentline, '^#\{1,6}') >= 0
    let header_level = strlen(substitute(currentline, '^\(#\{1,6}\).*', '\1', ''))
    return '>' . header_level
  endif
  let nextline = getline(v:lnum + 1)

  if match(currentline, '^\s*```') >= 0
    let next_line_is_code_block = synIDattr(synID(v:lnum + 1, 1, 1), 'name') ==# 'markdownFencedCodeBlock'
    if next_line_is_code_block
      return 'a1'
    endif
    return 's1'
  endif

  if (match(currentline, '^.*$') >= 0)
    if (match(nextline, '^=\+$') >= 0)
      return '>1'
    endif
    if (match(nextline, '^-\+$') >= 0)
      return '>2'
    endif
  endif

  return "="
endfunction

setlocal foldmethod=expr
setlocal foldexpr=MarkdownFolds()

" function! MarkdownFoldText()
"   let foldsize = (v:foldend-v:foldstart)
"   return getline(v:foldstart).' ('.foldsize.' lines)'
" endfunction
" setlocal foldtext=MarkdownFoldText()
