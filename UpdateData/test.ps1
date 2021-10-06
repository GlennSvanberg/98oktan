$headers=@{}
$headers.Add("Accept", "application/json, text/javascript, */*; q=0.01")
$headers.Add("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
$headers.Add("X-Requested-With", "XMLHttpRequest")
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$cookie = New-Object System.Net.Cookie
$cookie.Name = 'SSESS4b0dcc9eab24632c69fb1df50a2923c3'
$cookie.Value = 'vX2Do2U7R-6WmSJycZJNrxYxOMSksNElEk-gTsKtay9HMHLw'
$cookie.Domain = 'www.circlek.se'
$session.Cookies.Add($cookie)
$response = Invoke-WebRequest -Uri 'https://www.circlek.se/station-search?ajax_form=1' -Method POST -Headers $headers -WebSession $session -ContentType 'application/x-www-form-urlencoded; charset=UTF-8' -Body 'phrase=&EU_MILES_98=1&EU_MILESPLUS_98=1&form_build_id=form-icNimcBJKYBWZ3CRKJqUa6Hl8KQ_maoOcP4OyX3D4pY&form_id=sim_search_form&_triggering_element_name=op&_triggering_element_value=S%25C3%25B6k'