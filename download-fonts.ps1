$fontFiles = @(
    "fa-brands-400.woff2",
    "fa-brands-400.woff",
    "fa-brands-400.ttf",
    "fa-regular-400.woff2",
    "fa-regular-400.woff",
    "fa-regular-400.ttf",
    "fa-solid-900.woff2",
    "fa-solid-900.woff",
    "fa-solid-900.ttf"
)

$baseUrl = "https://use.fontawesome.com/releases/v5.15.3/webfonts/"

foreach ($file in $fontFiles) {
    $url = $baseUrl + $file
    $output = "static/webfonts/" + $file
    Write-Host "Downloading $file..."
    Invoke-WebRequest -Uri $url -OutFile $output
}

Write-Host "All font files downloaded successfully!" 