# Used in CI for nightly packaging

set -x
set -e

mvloc batch-apply $1
mvloc package $1

mv report.txt "packages/batch-apply-report-$1.txt"
mv writelist.json "packages/package-report-$1.json"
if [ -f ./metadata.xml/$1.xml ]; then
    cp "metadata.xml/$1.xml" "packages/metadata-$1.xml"
else
    cp "output-$1/mod-appendix/metadata.xml" "packages/metadata-$1.xml"
fi

pushd "output-$1"
zip -r "../packages/xml_only-$1.zip" *
popd
