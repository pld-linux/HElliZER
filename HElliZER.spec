Summary:	HElliZER - SDL demo
Summary(pl):	HElliZER - demo dla SDL-a
Name:		HElliZER
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://www.libsdl.org/projects/HElliZER/src/%{name}-%{version}.tar.gz
# Source0-md5:	f3192c24040eb30489c1045e990639fe
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-paths.patch
URL:		http://www.libsdl.org/projects/HElliZER/
BuildRequires:	SDL-devel >= 1.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HElliZER: the first portable demo in the world.

%description -l pl
HElliZER - pierwsze przeno¶ne demo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f acinclude.m4

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/dos

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install *.3d $RPM_BUILD_ROOT%{_datadir}/%{name}
install dos/HElliZER.EXE $RPM_BUILD_ROOT%{_datadir}/%{name}/dos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dos/{File_Id.Diz,HElliZER.NFO}
%attr(755,root,root) %{_bindir}/HElliZER
%{_datadir}/%{name}
