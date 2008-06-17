%define	real_name Mail-Transport-Dbx

Summary:	CPAN %{real_name} perl module
Name:		perl-%{real_name}
Version:	0.07
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/Mail-Transport-Dbx/
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod-Coverage
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Mail::Transport::Dbx is a wrapper around libdbx to read Outlook Express
mailboxes (more commonly known as .dbx files).

%prep
%setup -q -n %{real_name}-%{version}

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


