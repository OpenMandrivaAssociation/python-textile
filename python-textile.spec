%define shortname textile
Name:           python-%{shortname}
Version:        2.0.11
Release:        %mkrel 1
Summary:        A Humane Web Text Generator
Group:          Development/Python
License:        BSD
URL:            http://dealmeida.net/projects/textile/
Source0:        http://pypi.python.org/packages/source/t/%{shortname}/%{shortname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Textile is a XHTML generator using a simple markup developed by Dean Allen.
This is a Python port with support for code validation, itex to MathML
translation, Python code coloring and much more.

%prep
%setup -q -n %{shortname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
