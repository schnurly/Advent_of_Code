
$arrOpen = @('(','{','[','<')
$arrMap = @{')'='(';'}'='{';']'='[';'>'='<'}

function Score([string]$chr)
{
   if($chr -eq "(")
   {
     return 1
   }
   elseif($chr -eq "[")
   {
    return 2
   }
   elseif($chr -eq "{")
   {
    return 3
   }
   elseif($chr -eq "<")
   {
    return 4
   }
}

function isValid([string] $line)
{
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
          
            return $false
         }
      }   
   }
   return $true
}


$scoreList = [System.Collections.Generic.List[int64]]::New();
foreach($line in  Get-Content 'C:\temp\advent_input10.txt')
{
   
   if(isValid $line -eq $true)
   {
      Write-Host $line
      $replaced = $line
      
      Do
      {
        $reduced =$replaced
        $replaced = $replaced.Replace("()","").Replace("<>","").Replace("[]","").Replace("{}","")
      }While($replaced.Length -ne $reduced.Length)
      Write-Host $replaced
      $lineScore =0
      $chrArray = $replaced.ToCharArray()
      for($i=$chrArray.Length-1;$i-ge0;$i--)
      {
          $lineScore = $lineScore * 5 + $(Score $($chrArray[$i]))
      }
      Write-Host "LineScore:" $lineScore
      $scoreList.Add($lineScore)
   }
}

$mid = [int]$($scoreList.Count /2 )
$scoreList.Sort()
Write-Host $scoreList.Count
Write-Host $mid
Write-Host $scoreList[$mid]
Write-Host $scoreList[$mid-1]