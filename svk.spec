# TODO:
# - split into svk and perl-svk package
#
%include	/usr/lib/rpm/macros.perl
Summary:	SVK - a decentralized version control system
Summary(pl):	SVK - zdecentralizowany system kontroli wersji
Name:		svk
Version:	0.19
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Version Control
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVK-%{version}.tar.gz
# Source0-md5:	0a842eb28dbe1a8e450f68623b6cb1f6
URL:		http://svk.elixus.org/
BuildRequires:	perl-Algorithm-Annotate
BuildRequires:	perl-Algorithm-Diff
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl-File-MimeInfo
BuildRequires:	perl-Clone
BuildRequires:	perl-Data-Hierarchy >= 0.17
BuildRequires:	perl-Locale-Maketext-Lexicon
BuildRequires:	perl-Locale-Maketext-Simple
BuildRequires:	perl-PerlIO-via-dynamic >= 0.2
BuildRequires:	perl-PerlIO-via-symlink
BuildRequires:	perl-Pod-Escapes
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-Regexp-Shellish
BuildRequires:	perl-SVN-Mirror
BuildRequires:	perl-SVN-Simple
BuildRequires:	perl-Text-Diff
BuildRequires:	perl-YAML
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	perl-subversion >= 1.0.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
svk is a decentralized version control system. While Subversion (svn)
aims to take over the CVS user base, svk attempts to take over the
user base of the other version control systems, including people who
have already switched to another version control system, as well as
people who have not yet started using a version control system. It is
written in Perl and uses Subversion's underlying filesystem.

%description -l pl
svk to zdecentralizowany system kontroli wersji. O ile celem
Subversion (svn) jest przej�cie u�ytkownik�w CVS, svk pr�buje przej��
u�ytkownik�w innych system�w kontroli wersji, w��czaj�c ludzi kt�rzy
ju� przenie�li si� na inny system kontroli wersji, a tak�e ludzi,
kt�rzy jeszcze nie zacz�li u�ywa� systemu kontroli wersji. Jest
napisany w Perlu i u�ywa systemu plik�w Subversion.

%prep
%setup -q -n SVK-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[13]/*
%{perl_vendorlib}/SVK
%{perl_vendorlib}/SVK.pm
