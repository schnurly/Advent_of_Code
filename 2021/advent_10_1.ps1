
$arrOpen = @('(','{','[','<')
$arrMap = @{')'='(';'}'='{';']'='[';'>'='<'}

function Score([string]$chr)
{
   if($chr -eq ")")
   {
     return 3
   }
   elseif($chr -eq "]")
   {
    return 57
   }
   elseif($chr -eq "}")
   {
    return 1197
   }
   elseif($chr -eq ">")
   {
    return 25137
   }
}

$score=0
foreach($line in  Get-Content 'C:\temp\advent_input10.txt')
{
   $pos=0
   $list = [System.Collections.Generic.List[string]]::New();
   foreach($chr in $line.ToCharArray())
   {     
      [string]$sign = $chr
      if($arrOpen.Contains($sign))
      {  
         $list.Add($sign)
      }
      else
      {         
         if($arrMap[$sign] -eq $list[$list.Count-1])
         {
             $list.RemoveAt($list.Count-1)
         }
         else
         {
            $score += Score $sign
            Write-Host $line
            Write-Host "Failure at " $pos " : " $sign
            break
         }
      }
      $pos++
   }
}

Write-Host "Score:" $score