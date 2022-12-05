

$translation = [System.Collections.Generic.Dictionary[String,String]]::new();
$template=""
$isInstruction=$false
foreach($line in  Get-Content 'C:\temp\advent_input14.txt')
{
   if($line -eq "")
   {
      $isInstruction=$true
      continue
   }
   if($isInstruction -eq $false)
   {
     $template = $line  
   }
   else
   {
      $matches = [RegEx]::Matches($line,"(.+) -> (.+)") 
      $translation.Add($matches[0].Groups[1].Value,$matches[0].Groups[2].Value)
   }
}

foreach($key in $translation.Keys)
{
   Write-Host "Key:" $key " Value:" $translation[$key]
}

Write-Host "Template:" $template
for($i=0;$i-lt40;$i++)
{ 
   $workingTemplate = "" 
   $templateArr = $template.ToCharArray()
   for($index=0;$index-lt$template.Length-1;$index++)
   {
     if($translation.ContainsKey($templateArr[$index]+$templateArr[$index+1]))
     {
          $workingTemplate += $templateArr[$index] + $translation[$templateArr[$index]+$templateArr[$index+1]] 
     }
   }
  $workingTemplate += $templateArr[$template.Length-1]
  Write-Host "Step" $($i+1) ":" 
  $template = $workingTemplate
}
$count = [System.Collections.Generic.Dictionary[char,int64]]::new();
$templateArr = $template.ToCharArray()
foreach($chr in $templateArr)
{
     if(!$count.ContainsKey($chr))
     {
        $count.Add($chr,1)
     }
     else
     {
        $count[$chr]++
     }

}

$countHighest = [System.Tuple]::Create($templateArr[0],$count[$templateArr[0]])
$countLowest = [System.Tuple]::Create($templateArr[0],$count[$templateArr[0]])
foreach($key in $count.Keys)
{
   Write-Host "Key:" $key " Count:" $count[$key]
   if($countHighest.Item2 -lt $count[$key])
   { 
     $countHighest = [System.Tuple]::Create($key,$count[$key])
   }
   if($countLowest.Item2 -gt $count[$key])
   {
     $countLowest = [System.Tuple]::Create($key,$count[$key])
   }
}

Write-Host "H:" $countHighest.Item1 " C:" $countHighest.Item2
Write-Host "L:" $countLowest.Item1 " C:" $countLowest.Item2
Write-Host $($countHighest.Item2 -$countLowest.Item2)