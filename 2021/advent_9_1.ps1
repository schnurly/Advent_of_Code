$matrix = [System.Collections.Generic.List[int]]::New();
$cols=0
$rows=0
foreach($line in  Get-Content 'C:\temp\advent_input9.txt')
{
  $cols=0
  $rows++
  foreach($chr in $line.ToCharArray())
  {   
     $matrix.Add([convert]::ToInt32($chr, 10))
     $cols++
  }
}
Write-Host "Cols:" $cols
Write-Host "Rows:" $rows
$riskPoints=0
for($row=0;$row-lt$rows;$row++)
{  
   for($col=0;$col-lt$cols;$col++)
   {
       $i = ($row*$cols)+$col
       $current = $matrix[ $i]
       #Write-Host "current:"$current
       if($col -eq 0)
       {
         $prev = 10
       }
       else
       {
         $prev = $matrix[$i-1]
       }
       if(($col+1) -ge $cols)
       {
         $next = 10
       }
       else
       {
          $next = $matrix[$i+1]
       }
       if($row -eq 0)
       {
          $top = 10
       }
       else
       {
         $top = $matrix[$i - $cols]
       }
       
       if($row -eq ($rows-1))
       {
          $botton = 10
       }
       else
       {
         $botton = $matrix[$i + $cols]
         #Write-Host "botton:" +$botton
       }
       Write-Host "----------"
       Write-Host " " $top
       Write-host $prev $current $next
       Write-Host " " $botton
       #Write-Host $prev  $current  $next  $top $botton
       if($prev -gt $current -and $next -gt $current -and $top-gt $current -and $botton-gt$current)
       {
         Write-Host "Row:" $row " Number:" $current
         $riskPoints += ($current +1)
       }
       Write-Host "----------"
   }
}
Write-Host "RiskPoints:" $riskPoints