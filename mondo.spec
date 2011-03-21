#
# $Id: mondo.spec 1892 2008-03-22 00:57:27Z bruno $
#

Summary:	A program to create a rescue/restore CD/tape
Summary(fr):	Un programme pour créer un media de sauvegarde/restauration
Summary(it):	Un programma per utenti Linux per creare un CD/tape di rescue
Summary(sp):	Un programa por crear una CD/cinta de restoracion/rescate

Name:		mondo
Version:	2.29.5
%define upstreamv	2.2.9.5
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 1
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{upstreamv}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires:	newt-devel >= 0.50, gcc-c++, autoconf, automake, libtool
ExcludeArch:	ppc
Obsoletes: libmondo
Requires:	mindi >= 2.0.7, bzip2 >= 0.9, afio, mkisofs, binutils, newt >= 0.50, buffer, cdrecord,  
%ifarch ia64
Requires:	elilo, parted
%else
Requires:	syslinux >= 1.52
%endif

%description
Mondo is a GPL disaster recovery solution to create backup media 
(CD, DVD, tape, network images) that can be used to redeploy the 
damaged system, as well as deploy similar or less similar systems.

%prep
%setup -q -n %{name}-%{upstreamv}

%build
%configure2_5x
make %{?_smp_mflags} VERSION=%{version}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/%{_var}/cache/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog 
#svn.log
%doc INSTALL COPYING README* TODO AUTHORS NEWS*
%doc docs/en/mondorescue-howto.html docs/en/mondorescue-howto.pdf

%{_sbindir}/*
%{_datadir}/%{name}
%{_mandir}/man8/*
%{_var}/cache/%{name}

%changelog
