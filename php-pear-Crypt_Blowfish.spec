%define		_class		Crypt
%define		_subclass	Blowfish
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.1
Release:	14
Summary:	Quick two-way blowfish encryption
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Crypt_Blowfish/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
BuildRequires:	sed >= 4.0.0
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package allows you to preform two-way blowfish on the fly using
only PHP. This package does not require the Mcrypt PHP extension to
work.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-12mdv2012.0
+ Revision: 741832
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-11
+ Revision: 679271
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-10mdv2011.0
+ Revision: 613620
- the mass rebuild of 2010.1 packages

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-9mdv2010.1
+ Revision: 478298
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2010.0
+ Revision: 440952
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 321937
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2009.0
+ Revision: 236813
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.0.1-5mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdv2007.0
+ Revision: 81420
- Import php-pear-Crypt_Blowfish

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- 1.0.1

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

