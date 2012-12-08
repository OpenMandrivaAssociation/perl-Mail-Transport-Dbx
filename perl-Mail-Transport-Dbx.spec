%define	upstream_name    Mail-Transport-Dbx
%define	upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Mail-Transport-Dbx/
Source0:	http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod-Coverage
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Mail::Transport::Dbx is a wrapper around libdbx to read Outlook Express
mailboxes (more commonly known as .dbx files).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/*/Mail/Transport
%{perl_vendorlib}/*/auto/Mail/Transport


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-6mdv2012.0
+ Revision: 765473
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-5
+ Revision: 763958
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-4
+ Revision: 667256
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.70.0-3mdv2011.0
+ Revision: 564532
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 556001
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 403845
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.07-6mdv2009.0
+ Revision: 223815
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.07-5mdv2008.1
+ Revision: 151417
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.07-4mdv2007.1
+ Revision: 138900
- use the %%mkrel macro

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Mail-Transport-Dbx

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.07-3mdk
- Rebuild

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.07-2mdk
- fix deps

* Sat Jul 09 2005 Andreas Hasenack <andreas@mandriva.com> 0.07-1mdk
- packaged for Mandriva

