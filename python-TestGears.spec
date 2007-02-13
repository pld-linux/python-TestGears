
%define	module	TestGears

Summary:	TestGears extensions to unittest
Summary(pl.UTF-8):	Rozszerzenie TestGears do unittest
Name:		python-TestGears
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.turbogears.org/download/eggs/%{module}-%{version}.tar.gz
# Source0-md5:	1911b1555cf8869e14d1f71da590bc0e
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

%description -l pl.UTF-8
TestGears udostępnia automatyczne wykrywanie unittest.TestCases i
możliwość uruchamiania testów napisanych jako proste funkcje. Generuje
standardowy unittest.TestSuite do używania z dowolnym ze standardowych
frontendów i udostępnia polecenie distutils do uruchamiania testów bez
żadnej konfiguracji.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
        --single-version-externally-managed \
        --optimize 2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/test*
