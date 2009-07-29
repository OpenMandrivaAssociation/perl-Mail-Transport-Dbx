%define	upstream_name    Mail-Transport-Dbx
%define	upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/*/Mail/Transport
%{perl_vendorlib}/*/auto/Mail/Transport
