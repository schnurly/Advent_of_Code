class Point
{
  [int]$X
  [int]$Y
  Point([int]$X,[int]$Y)
  {
     $this.X = $X
     $this.Y = $Y
  }
}

class Fold
{
  [int]$Position
  [string]$Axe
  Fold([int]$Position,[string]$Axe)
  {
     $this.Position = $Position
     $this.Axe = $Axe
  }
}


$points = [System.Collections.Generic.List[Point]]::new();
$folds = [System.Collections.Generic.List[Fold]]::new();

$isFoldInstruction=$false
foreach($line in  Get-Content 'C:\temp\advent_input13.txt')
{
   if($line -eq "")
   {
      $isFoldInstruction=$true
      continue
   }
   if($isFoldInstruction -eq $false)
   {
     $arr = $line.split(",")
     $point = [Point]::new($arr[0],$arr[1]);
     #Write-Host "create point x:" $point.X " Y:" $point.Y
     $points.Add($point)
   }
   else
   {
     $matches = [regex]::Matches($line, "fold along ([a-z])=([0-9]+)")
     [string]$axe = $matches[0].Groups[1].Value     
     [int]$pos = $matches[0].Groups[2].Value   
     $fold = [Fold]::new($pos,$axe);
     $folds.Add($fold)
   }
   
}

$bigX = 0
$bigY = 0

foreach($fold in $folds)
{
    if(0 -eq $bigX -and $fold.Axe -eq "x")
    {
      $bigX = $fold.Position * 2
    }
    if(0 -eq $bigY -and $fold.Axe -eq "y")
    {
      $bigY = $fold.Position * 2
    }
}

Write-Host "Matrix Size X:" $bigX " Y:" $bigY

$matrix = [System.Collections.Generic.List[System.Collections.Generic.List[int]]]::new();
for($y=0;$y-le$bigY;$Y++)
{
   $row = [System.Collections.Generic.List[int]]::new();
   for($x=0;$x-le$bigX;$x++)   
   {
     $row.Add(0) 
   }
   $matrix.Add($row)
}
foreach($point in $points)
{
  $matrix[$point.Y][$point.X] = 1
}

foreach($row in $matrix)
{
  #Write-Host $row
}

foreach($fold in $folds)
{
   Write-Host "Fold " $fold.Axe " on " $fold.Position
   $bigX = $matrix[0].Count -1 
   $bigY = $matrix.Count -1 

  $newmatrix = [System.Collections.Generic.List[System.Collections.Generic.List[int]]]::new();

  if($fold.Axe -eq "y")
  {
    for($z=0;$z-lt$fold.Position;$z++){
       $row = [System.Collections.Generic.List[int]]::new();
       for($x=0;$x-le$bigX;$x++)  
       {
         $row.Add($($matrix[$z][$x] + $matrix[$bigY-$z][$x]))
       }
       $newmatrix.Add($row)
    }
  }
  else
  {
    for($y=0;$y-le$bigY;$y++) 
    {
       $row = [System.Collections.Generic.List[int]]::new();
       for($z=0;$z-lt$fold.Position;$z++) 
       {
         $row.Add($($matrix[$y][$z] + $matrix[$y][$bigX-$z]))
       }
       $newmatrix.Add($row)
    }
   }
   $matrix = $newmatrix   
}


for($y=0;$y-lt$matrix.Count;$y++){
  for($x=0;$x-lt$matrix[$y].Count;$x++){
   if($matrix[$y][$x] -ge 1)
   {
     $matrix[$y][$x] = 1
   }
  }
}


Write-Host "New Matrix"

$dots=0
$newX=0
$newY=0
foreach($row in $newmatrix)
{
 $newY++
 Write-Host $row
 $newX=0
  foreach($col in $row)
  {
    $newX++
    if($col -gt 0 )
    {
       $dots++
    }
  }
}
Write-Host "NewX Count:" $newX
Write-Host "NewY Count:" $newY
Write-Host "Dots:" $dots