#
# $Id: mondo.spec 1892 2008-03-22 00:57:27Z bruno $
#

Summary:	A program to create a rescue/restore CD/tape
Summary(fr):	Un programme pour créer un media de sauvegarde/restauration
Summary(it):	Un programma per utenti Linux per creare un CD/tape di rescue
Summary(sp):	Un programa por crear una CD/cinta de restoracion/rescate

Name:		mondo
Version:	2.29.3
%define upstreamv	2.2.9.3
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 2
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

%description -l fr
Objectif
""""""""
Mondo est une solution GPL de sauvegarde en cas de désastre pour 
créer des médias (CD, DVD, bande, images réseau) qui peuvent être 
utilisés pour redéployer le système endomangé, aussi bien que des 
systèmes similaires, ou moins similaires.

%description -l it
Scopo
"""""
Mondo e' un programma che permette a qualsiasi utente Linux 
di creare un cd di rescue/restore (o piu' cd qualora l'installazione 
dovesse occupare piu' di 2Gb circa). Funziona con gli azionamenti di
nastro, ed il NFS, anche.

%description -l sp
Objectivo
"""""""""
Mondo es un programa que permite cualquier usuario de Linux a crear una CD
de restoracion/rescate (o CDs, si su instalacion es >2GO aprox.).  Funciona 
con cintas y NFS, tambien.

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
