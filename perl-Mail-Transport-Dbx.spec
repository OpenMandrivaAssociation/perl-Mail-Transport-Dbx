%define	modname	Mail-Transport-Dbx
%define	modver	0.07

Summary:	CPAN %{modname} perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Mail-Transport-Dbx/
Source0:	http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod-Coverage

%description
Mail::Transport::Dbx is a wrapper around libdbx to read Outlook Express
mailboxes (more commonly known as .dbx files).

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*/Mail/Transport
%{perl_vendorlib}/*/auto/Mail/Transport
%{_mandir}/man3/*

