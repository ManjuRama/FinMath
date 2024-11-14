{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPFXwXrd0QjYD4jAg0miTb0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ManjuRama/FinMath/blob/main/test.cmd\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "pz_eIEHasReV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Define the input and output directories\n",
        "$inputDir = \"C:\\path\\to\\your\\doc\\files\"  # Replace with your directory path\n",
        "$outputDir = $inputDir                   # Output in the same directory\n",
        "\n",
        "# Create a Word application object\n",
        "$word = New-Object -ComObject Word.Application\n",
        "$word.Visible = $false\n",
        "\n",
        "# Loop through each .doc and .docx file in the directory\n",
        "Get-ChildItem -Path $inputDir -Filter *.doc* | ForEach-Object {\n",
        "    $docPath = $_.FullName\n",
        "    $pdfPath = Join-Path -Path $outputDir -ChildPath ($_.BaseName + \".pdf\")\n",
        "\n",
        "    # Open the document\n",
        "    $doc = $word.Documents.Open($docPath)\n",
        "\n",
        "    # Save as PDF\n",
        "    $doc.SaveAs([ref] $pdfPath, [ref] 17)  # 17 is the format for PDF in Word\n",
        "\n",
        "    # Close the document\n",
        "    $doc.Close()\n",
        "    Write-Output \"Converted $($_.Name) to PDF.\"\n",
        "}\n",
        "\n",
        "# Quit Word application\n",
        "$word.Quit()\n"
      ],
      "metadata": {
        "id": "0f12_pYksSR5"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}