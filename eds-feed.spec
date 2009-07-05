%define galagod_version	0.5.0
%define galago_version	0.5.0
%define eds_version		1.1.4
%define glib2_version	2.4.0
Summary:	Evolution Data Server feed for Galago
Name:		eds-feed
Version:	0.5.0
Release: %mkrel 8
License:	GPLv2+
Group:		System/Servers
URL:		http://www.galago-project.org/
Source:		http://www.galago-project.org/files/releases/source/eds-feed/%{name}-%{version}.tar.bz2
Patch: eds-feed-0.5.0-new-eds.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires: libgalago-devel             >= %{galago_version}
BuildRequires: evolution-data-server-devel >= %{eds_version}
BuildRequires: glib2-devel                 >= %{glib2_version}
BuildRequires: libxml2-devel

%description
A feed for Galago that uses contact entries in the Evolution address book
to link people and accounts.


%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make


%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS 
%{_libexecdir}/galago/eds-feed


