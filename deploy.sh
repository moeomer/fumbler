workon pdf
mkdir pdf
pip install  --target ./pdf -r requirements.txt
cp *.py ./pdf
cp *.xsl ./pdf
cp -r binary/ pdf/binary
cd pdf
zip -r pdf.zip *
aws lambda update-function-code --function-name generated_pdfs --zip-file fileb://pdf.zip
cd ..
rm -rf pdf
rm -rf pdf.zip