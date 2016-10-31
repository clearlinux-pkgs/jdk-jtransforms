Name     : jdk-jtransforms
Version  : 2.4.0
Release  : 4
URL      : https://repo1.maven.org/maven2/com/github/rwl/jtransforms/2.4.0/jtransforms-2.4.0.jar
Source0  : https://repo1.maven.org/maven2/com/github/rwl/jtransforms/2.4.0/jtransforms-2.4.0.jar
Source1  : https://repo1.maven.org/maven2/com/github/rwl/jtransforms/2.4.0/jtransforms-2.4.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MPL-2.0
Requires: jdk-jtransforms-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jtransforms package.
Group: Data

%description data
data components for the jdk-jtransforms package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jtransforms.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jtransforms.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jtransforms.xml \
%{buildroot}/usr/share/maven-poms/jtransforms.pom \
%{buildroot}/usr/share/java/jtransforms.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jtransforms.jar
/usr/share/maven-metadata/jtransforms.xml
/usr/share/maven-poms/jtransforms.pom
