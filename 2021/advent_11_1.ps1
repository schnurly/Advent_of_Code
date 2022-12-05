
$map = [System.Collections.Generic.List[System.Collections.Generic.List[int]]]::New();
foreach($line in  Get-Content 'C:\temp\advent_input11.txt')
{
   $row = [System.Collections.Generic.List[int]]::New();
   foreach($chr in $line.ToCharArray())
   {
      $num = [convert]::ToInt32($chr, 10)
      $row.Add($num)
   }
   $map.Add($row)
}
function increment()
{
  for($row=0;$row-lt$map.Count;$row++){
  for($col=0;$col-lt$map[$row].Count;$col++)
  {     
    $map[$row][$col]++
  }
  }
}

function checkNull()
{
  $sum=0
  for($row=0;$row-lt$map.Count;$row++){
  for($col=0;$col-lt$map[$row].Count;$col++)
  {     
    $sum = $map[$row][$col]
    if($sum -gt 0)
    {
      return $sum
    }
  }
  }
  return $sum
}

function print()
{
   Write-Host "----------------------------"
  foreach($row in $map)
    {
        Write-Host $row

    }
    Write-Host "----------------------------"
}

function countUp([int]$value)
{
   if($value -gt 0)
   {
     return $value +1
   }
   return $value
}

function doBlink()
{
for($row=0;$row-lt$map.Count;$row++){
  for($col=0;$col-lt$map[$row].Count;$col++)
  {     
     if($map[$row][$col] -ge 10)
     {
         Write-Host "Blink"
         if($col -gt 0)
         {
            $map[$row][$col-1] = countUp $map[$row][$col-1] 
            if($row -gt 0)
            {
               $map[$row-1][$col-1] = countUp $map[$row-1][$col-1]               
            }
            if($row-lt $map[$row].Count -1)
            {
               $map[$row+1][$col-1] = countUp $map[$row+1][$col-1]      
            }
         }   
       
        if($row -gt 0)
        {               
            $map[$row-1][$col] = countUp $map[$row-1][$col] 
        }
         
        if($row-lt $map[$row].Count -1)
        {         
            $map[$row+1][$col] = countUp $map[$row+1][$col]
        }

         if($col -lt $map[$row].Count -1)
         {
            $map[$row][$col+1] = countUp $map[$row][$col+1]
            if($row -gt 0)
            {
               $map[$row-1][$col+1] = countUp $map[$row-1][$col+1]              
            }
            if($row-lt $map[$row].Count -1)
            {
               $map[$row+1][$col+1] = countUp $map[$row+1][$col+1]          
            }
         }      
         $map[$row][$col] = 0    
         return $true
     }
  }
}
return $false
}


$flashCount=0
print
for($step=1;$step-le1000;$step++)
{
  Write-Host "Step:"$step
  $doNextBlink= $true  
  increment 

  do
  {
 
    $doNextBlink = doBlink  
  
    if($doNextBlink -eq $true)
    {
       $flashCount++
    }
  }
  while($doNextBlink)
  print
  
  $sum = checkNull
  Write-host "sum:" $sum
  if($sum  -eq 0)
  {
     break
  }
}

Write-host "flashes:" $flashCount