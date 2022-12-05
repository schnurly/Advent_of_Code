$matrix = [System.Collections.Generic.List[int]]::New();
$cols=0
$rows=0
foreach($line in  Get-Content 'C:\temp\advent_input9_2.txt')
{
  $cols=0
  $rows++
  foreach($chr in $line.ToCharArray())
  {   
     $matrix.Add([convert]::ToInt32($chr, 10))
     $cols++
  }
}

function travBasin([int]$row,[int]$col){
   $i = ($row*$cols)+$col
   $current = $matrix[$i]   
   $size = [System.Collections.Generic.List[int]]::New()
   if($current -eq 9)
   { 
     return $size
   }
   $size.Add($i)
   if($row -gt 0)
   {
      $pos = $i -$cols
      $top = $matrix[ $pos]
      if($top -eq $current+1 )
      {  
       
         $travList =  travBasin $($row-1) $col 
         foreach($trav in $travList)
         { 
           if(!$size.Contains($trav))
           {
           
              $size.Add($trav)
           }
         }
      }
   }
   if($row -lt $rows -1)
   {
      $pos =  $i +$cols
      $down = $matrix[$pos]
      if($down -eq $current+1 )
      {  
        
           $travList = travBasin $($row+1) $col  
            foreach($trav in $travList)
         { 
           if(!$size.Contains($trav))
           {
        
              $size.Add($trav)
           }
         }
      }
   }
   if($col -gt 0)
   {
      $pos =  $i -1
      $left = $matrix[ $pos]
      if($left -eq $current+1 )
      {  
           
           $travList = travBasin $row $($col-1) 
         foreach($trav in $travList)
         { 
           if(!$size.Contains($trav))
           {
         
              $size.Add($trav)
           }
         }
      }
   }
   if($col -lt $cols-1){
     $pos =  $i +1
     $right = $matrix[ $pos]
      if($right -eq $current+1 )
      {  
           
           $travList = travBasin $row $($col+1) 
            foreach($trav in $travList)
         { 
           if(!$size.Contains($trav))
           {
           
              $size.Add($trav)
           }
         }
      }
   }
   return $size
}

$basinCounts = [System.Collections.Generic.List[int]]::New()
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
       }
       #Write-Host "----------"
       #Write-Host " " $top
       #Write-host $prev $current $next
       #Write-Host " " $botton
       #Write-Host "----------"

       if($prev -gt $current -and $next -gt $current -and $top-gt $current -and $botton-gt$current)
       {
         #Write-Host "Row:" $row " Number:" $current
         $size = travBasin $row $col 
         Write-Host "BasinSize:"   $size.Count
         $basinCounts.Add($size.Count)
       }
     
   }
}

$basinCounts.Sort()
Write-Host $basinCounts[$basinCounts.Count-1]
Write-Host $basinCounts[$basinCounts.Count-2]
Write-Host $basinCounts[$basinCounts.Count-3]
Write-Host  $($basinCounts[$basinCounts.Count-1] * $basinCounts[$basinCounts.Count-2] * $basinCounts[$basinCounts.Count-3])