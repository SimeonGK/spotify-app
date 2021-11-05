$buttonStart_Click = {
    $rows = Get-Content C:\Users\cemay\Desktop\spotify_dataset.csv
 
    for ($i = 0; $i -lt $rows.count; $i++) {
        $thisrow = $rows[$i] -split ","
        for ($j = 0; $j -lt $thisrow.count; $j++) {
            (Get-Variable -Name "Textbox$i$j").Value.Text = $thisrow[$j]
        }
    }
}