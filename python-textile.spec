%define shortname textile
Name:           python-%{shortname}
Version:        2.1.5
Release:        %mkrel 1
Summary:        A Humane Web Text Generator
Group:          Development/Python
License:        BSD
URL:            http://dealmeida.net/projects/textile/
Source0:        http://pypi.python.org/packages/source/t/%{shortname}/%{shortname}-%{version}.tar.gz

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
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*


%changelog
* Sat May 07 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.1.5-1mdv2011.0
+ Revision: 672278
- new version 2.1.5

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 2.1.4-2mdv2011.0
+ Revision: 590588
- rebuild for python 2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.4-1mdv2010.1
+ Revision: 489195
- update to new version 2.1.4

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.3-1mdv2010.0
+ Revision: 384258
- update to new version 2.1.3

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 2.0.11-5mdv2009.1
+ Revision: 323413
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.0.11-4mdv2009.0
+ Revision: 259833
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.0.11-3mdv2009.0
+ Revision: 247699
- rebuild
- fix description-line-too-long
- fix summary
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 21 2007 Colin Guthrie <cguthrie@mandriva.org> 2.0.11-1mdv2008.1
+ Revision: 100743
- BuildRequires python-setuptools
- import python-textile


