%define shortname textile
%define debug_package %{nil}

Name:           python-%{shortname}
Version:        2.1.8
Release:        2
Summary:        A Humane Web Text Generator

Group:          Development/Python
License:        BSD
URL:            https://dealmeida.net/projects/textile/
Source0:        http://pypi.python.org/packages/source/t/textile/textile-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Textile is a XHTML generator using a simple markup developed by Dean Allen.
This is a Python port with support for code validation, itex to MathML
translation, Python code coloring and much more.

%prep
%setup -q -n %{shortname}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}
 
%files
%{py_platsitedir}/*

