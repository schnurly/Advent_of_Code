

$count =0

function containsLetter($text, $pattern )
{
   foreach($chr in $pattern.ToCharArray())
   { 
      if(!$text.contains($chr))
      {
         return $false
      }
   }
   return $true
}

$resultNumber = 0
foreach($line in  Get-Content 'C:\temp\advent_input8.txt')
{
   $numbers = [System.Collections.Generic.List[string]]::New();
   Write-Host "Block:" $line
   $block = $line.Split("|")
   Write-Host "Right:" $block[1]
   foreach($number in $block[0].Split(" "))
   {
      $numbertrimed = $number.Trim()
     
      if($numbertrimed.Length -eq 2)
      {
        $one = $numbertrimed
      }
      elseif($numbertrimed.Length -eq 3)
      {
        $seven = $numbertrimed
      }
      elseif($numbertrimed.Length -eq 4)
      {
        $four = $numbertrimed
      }
      elseif($numbertrimed.Length -eq 7)
      {
        $eigth = $numbertrimed
      }
      else
      {
        $numbers.Add($numbertrimed)
      }
   }
   $two = ""
   $three =""
   $five =""
   $six=""
   $nine=""
   $zero=""

   $top = $seven
   foreach($s in $one.ToCharArray())
   {
     $top = $top.Replace($s.ToString(),"")
   }
   $matcheCount = 0
   for($i=0;$i-le10;$i++)
   {
       $toremovenumbers = [System.Collections.Generic.List[string]]::New();
       foreach($number in $numbers)
       {
          if($number.Length -eq 6)
          {
             if(containsLetter $number $four)
             {    
                $nine = $number                $toremovenumbers.Add($number)
             }
             elseif((containsLetter $number$one $eigth))
             {           
                $six = $number
                $toremovenumbers.Add($number)
             }
             if(($nine -ne "") -and ($six -ne ""))
             {
                $zero = $number
                $toremovenumbers.Add($number)
             }
          }
          elseif($number.Length -eq 5)
          {
             if(containsLetter $number $one )
             {            
                $three = $number
                $toremovenumbers.Add($number)
             } 
             elseif((containsLetter $number$one $nine ) -and ($nine -ne ""))
             {
                Write-Host $number$one " " $nine
                $five = $number
                $toremovenumbers.Add($number)
             }      
          }
       }
       foreach($number in $toremovenumbers)
       {
         $numbers.Remove($number)
       }
   }
   $two = $numbers[0]
$decoded = @($zero,$one,$two,$three,$four,$five,$six,$seven,$eigth,$nine)
Write-Host "1:" $one
Write-Host "2:" $two
Write-Host "3:" $three
Write-Host "4:" $four
Write-Host "5:" $five
Write-Host "6:" $six
Write-Host "7:" $seven
Write-Host "8:" $eigth
Write-Host "9:" $nine
Write-Host "0:" $zero

   $finalNumber = ""
   foreach($number in $block[1].Split(" "))
   {
      $numbertrimed = $number.Trim()
      for($i=0;$i-lt $decoded.Count;$i++)
      {  
         $found = $false 
         if($decoded[$i].Length -eq $numbertrimed.Length)
         {  
            $found = $true 
            foreach($chr in $decoded[$i].ToCharArray())
            {
             
               if(!$numbertrimed.Contains($chr))
               {               
                 $found = $false
                 break
               }
            }
         }
         if($found -eq $true)
         {  
            #Write-Host "Number: " $numbertrimed " "  $i
            $finalNumber += "" + $i
            break
         }
      }
   }
   Write-Host "Number" $finalNumber
   $resultNumber += [int]$finalNumber
}
Write-Host "Result:" $resultNumber