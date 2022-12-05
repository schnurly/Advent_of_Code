
$oneCount = [System.Collections.Generic.List[int]]::New();
$linesCount = 0;
foreach($line in  Get-Content 'C:\temp\advent_input3.txt')
{
   if($oneCount.Count -eq 0)
   {
     foreach($chr in  $line.toCharArray())
     {
       $oneCount.Add(0)
     }
   }

   $charArray = $line.toCharArray()
   for($i=0;$i -lt $charArray.Count;$i++)
   {
      if($charArray[$i] -eq "1")
      { 
        $oneCount[$i] += 1
      }
   }
   $linesCount++
}

Write-Host "LinesCount: " $linesCount

[string]$gamma = ""
[string]$espilon = ""
foreach($bytepos in $oneCount)
{
  Write-Host $bytepos
   if($bytepos -gt ( $linesCount /2))
   { 
      $gamma += "1"
      $espilon +="0"
   }
   else
   {
     $gamma += "0"
     $espilon +="1"
   }
}
Write-Host $gamma
$gammeInt = [convert]::ToInt32($gamma,2)

Write-Host $espilon
$espilonInt = [convert]::ToInt32($espilon,2)

Write-Host ($gammeInt *$espilonInt)