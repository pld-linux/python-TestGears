
%define	module	TestGears

Summary:	TestGears extensions to unittest
Summary(pl):	Rozszerzenie TestGears do unittest
Name:		python-TestGears
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.turbogears.org/download/eggs/TestGears-%{version}-py2.4.egg
# Source0-md5:	2c9393c63bafa0c69d781eb9458febe5
URL:		http://www.turbogears.org/testgears/
%pyrequires_eq	python
BuildRequires:	python-devel
BuildRequires:	unzip
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TestGears provides automatic discovery of unittest.TestCases and the
ability to run tests that are written as simple functions. It
generates a standard unittest.TestSuite for use with any of the
standard frontends, and provides a distutils command to run tests with
zero configuration.

%description -l pl
TestGears udostêpnia automatyczne wykrywanie unittest.TestCases i
mo¿liwo¶æ uruchamiania testów napisanych jako proste funkcje. Generuje
standardowy unittest.TestSuite do u¿ywania z dowolnym ze standardowych
frontendów i udostêpnia polecenie distutils do uruchamiania testów bez
¿adnej konfiguracji.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

%{_bindir}/easy_install \
	--no-deps \
	--script-dir="$RPM_BUILD_ROOT%{_bindir}" \
	--install-dir="$RPM_BUILD_ROOT%{py_sitescriptdir}" \
	--always-unzip \
	%{SOURCE0}

%py_postclean

echo '%{module}-%{version}-py%{py_ver}.egg' > $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}*
